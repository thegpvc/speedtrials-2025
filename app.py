import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# Data storage
water_systems_data = []

# Plain English explanations for violation types
VIOLATION_EXPLANATIONS = {
    "MCL Exceedance (Lead)": "Levels of lead were higher than the Maximum Contaminant Level (MCL) allowed. Lead can cause serious health problems, especially for pregnant women and young children.",
    "Monitoring Failure": "The water system failed to conduct required water quality monitoring or report results correctly. This means potential issues might not have been detected.",
    "Disinfection Byproduct": "Levels of disinfection byproducts (formed when disinfectants react with organic matter in water) were too high. Some byproducts may increase health risks over long periods.",
    "High Turbidity": "Turbidity (cloudiness of water) was too high. High turbidity can interfere with disinfection and provide a medium for microbial growth.",
    "N/A": "No specific violation type applicable or no recent violations."
    # Add more as needed
}

def get_status_details(system_data):
    """Determines status color and provides plain English summary."""
    status = system_data.get('OverallStatus', 'Unknown').lower()
    violations_count = int(system_data.get('ViolationsLast2Years', 0))
    last_violation_type = system_data.get('LastViolationType', 'N/A')

    details = {
        "color": "grey", # Default
        "summary_text": "Status information is currently unavailable.",
        "violation_explanation": VIOLATION_EXPLANATIONS.get(last_violation_type, "No specific explanation available for this violation type.")
    }

    if status == 'green':
        details['color'] = 'green'
        details['summary_text'] = "This water system currently meets safety standards based on available data."
        if violations_count == 0:
             details['violation_explanation'] = "No violations reported in the last 2 years."
    elif status == 'yellow':
        details['color'] = 'yellow'
        details['summary_text'] = "This water system has had some issues or minor violations. Check details below."
    elif status == 'red':
        details['color'] = 'red'
        details['summary_text'] = "This water system has significant or recent violations. Caution is advised. Review details carefully."

    # If status was determined by violation count in CSV, that's fine
    # Otherwise, this provides a more dynamic status based on mock data fields
    if violations_count > 3:
         details['color'] = 'red'
         details['summary_text'] = "This water system has a high number of violations. Review details carefully."
    elif violations_count > 0:
        if details['color'] != 'red': # Don't override red if it's already set
            details['color'] = 'yellow'
            details['summary_text'] = "This water system has had some violations. Check details below."

    return details

def load_data():
    """Loads data from the CSV file into memory."""
    global water_systems_data
    try:
        with open('mock_sdwis_data.csv', mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            water_systems_data = [row for row in reader]
        print(f"Loaded {len(water_systems_data)} water systems.")
    except FileNotFoundError:
        print("ERROR: mock_sdwis_data.csv not found. Please create it.")
        water_systems_data = []
    except Exception as e:
        print(f"Error loading data: {e}")
        water_systems_data = []

@app.before_request
def ensure_data_loaded():
    # This runs before every request, but load_data() itself is idempotent
    # For a real app, consider loading once at startup or using a more robust data store.
    # @app.before_first_request is better but can be tricky with some Flask reloader setups.
    if not water_systems_data: # Only load if it's empty
        load_data()


@app.route('/')
def index():
    system_names = sorted(list(set(row['WaterSystemName'] for row in water_systems_data if 'WaterSystemName' in row)))
    return render_template('index.html', message='Select your water system to check its status:', systems=system_names)

@app.route('/lookup', methods=['POST'])
def lookup():
    selected_system_name = request.form.get('system_select')
    system_info_raw = None
    if selected_system_name:
        for system in water_systems_data:
            if system.get('WaterSystemName') == selected_system_name:
                system_info_raw = system
                break

    if system_info_raw:
        status_details = get_status_details(system_info_raw)
        # For violation timeline, we'd need more structured data (e.g., a list of violations)
        # For now, the timeline aspect is covered by "LastViolationDate" and "LastViolationType"
        return render_template('results.html', system=system_info_raw, status=status_details)
    else:
        system_names = sorted(list(set(row['WaterSystemName'] for row in water_systems_data if 'WaterSystemName' in row)))
        return render_template('index.html', message=f"System '{selected_system_name}' not found. Please try again.", error=True, systems=system_names)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
