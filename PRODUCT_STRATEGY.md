# Product Strategy: Georgia's Public Trust & Compliance Platform

## 1. Executive Summary: The "Secret Memo"

**The Situation:** The Georgia Environmental Protection Division (EPD) is not just upgrading a website; it is responding to a full-blown crisis of public trust. Widespread fear over PFAS "forever chemicals," amplified by high-profile lawsuits in communities like Calhoun and Augusta, has put the agency under immense pressure. The current drinking water portal, `gadrinkingwater.net`, is a relic—an expert-only tool that is opaque and unusable for the average citizen, further eroding public confidence. Compounding this is a new, unfunded federal mandate from the EPA that establishes legally enforceable limits for PFAS, creating a significant compliance burden for the EPD.

**The Mission:** This project is a search for a strategic solution to two problems: a political problem (public mistrust) and a technical problem (federal compliance). We must deliver a **"Public Trust and Compliance Platform"** that is both a powerful tool for public transparency and an efficient system for internal data management.

**The Decision-Maker:** The RFI's issuing officer, Rhonda Henslee, is the Chief Procurement Officer for the DNR. She is not an environmental scientist. Her primary drivers are fiscal responsibility, risk mitigation, and delivering clear, auditable value. Our solution must be framed to appeal to these priorities.

**The Strategic Recommendation:** We will propose a turnkey platform that solves the EPD's dual crisis.
1.  **For the Public (The "Trust" Component):** An intuitive, map-centric public portal inspired by the best features of the EWG and Airbnb. It will allow any citizen to enter their address and see a clear, color-coded "scorecard" for their water quality.
2.  **For the EPD (The "Compliance" Component):** A streamlined administrative backend to automate the data ingestion, management, and reporting required by the new EPA PFAS rule.

This approach positions our solution as the only one that understands the high-stakes, behind-the-scenes context of this RFI. It demonstrates not just technical competence, but strategic wisdom.

## 2. Product Vision & Guiding Principles

Our vision is to create the most trusted and transparent resource for drinking water information in Georgia.

*   **Principle 1: Simplicity Builds Trust.** We will answer the public's primary question—"Is my water safe?"—immediately and clearly. No jargon, no complex charts on the landing page.
*   **Principle 2: Empower, Don't Just Inform.** We will provide users with actionable steps they can take to protect their families, inspired by the EWG's water filter guide.
*   **Principle 3: Design for Transparency.** Our interface will be clean, modern, and intuitive, drawing inspiration from best-in-class consumer applications like Airbnb and the visual clarity of the NYC and Texas portals.
*   **Principle 4: Mobile-First.** All features will be designed for a seamless experience on any device, ensuring accessibility for all users, including regulators in the field.

## 3. Feature Roadmap & Technical Considerations

### Phase 1: The Public-Facing MVP (The "Trust" Platform)

| Feature | Description | Technical Considerations |
| :--- | :--- | :--- |
| **V1: Address-Based Search & Map** | A prominent, single search bar where users can enter their address. The results will be displayed on a clean, interactive map, similar to Airbnb's search experience. | - Geocoding API (e.g., Mapbox, Google Maps) to convert addresses to coordinates. <br> - Reverse geocoding to match coordinates to water system service areas. <br> - Interactive map library (e.g., Leaflet, Mapbox). |
| **V1: The "Water Scorecard"** | Upon searching, the user is presented with a simple, visually intuitive "scorecard" for their water system. This will use a clear color-coded system (e.g., Green, Yellow, Red) to answer "Is my water safe?". | - Algorithm to calculate a "risk score" based on violation history and contaminant levels relative to MCLs. <br> - The UI will be the primary focus, ensuring it is beautiful, trustworthy, and easy to understand. |
| **V2: The "Drill-Down"** | For users who want more detail, a clear "Learn More" button will reveal a more detailed view, including: <br> - **Contaminant Details:** Plain-language explanations of detected contaminants, their health effects, and a comparison to MCLs. <br> - **Violation History:** A simple timeline of past violations. | - Join `SDWA_LCR_SAMPLES.csv` and `SDWA_VIOLATIONS_ENFORCEMENT.csv` with `EPA_MCLS.csv`. <br> - The UI for this section can include simple charts and graphs, but they will be secondary to the main scorecard. |
| **V3: Actionable Guidance** | Inspired by the EWG, we will provide users with a simple guide to common water filters and other actions they can take to reduce their exposure to specific contaminants. | - This can be a static content page initially, with the potential for a more personalized guide in the future. |

### Phase 2: The Operator & Regulator Toolkit (The "Compliance" Platform)

| Feature | Description | Technical Considerations |
| :--- | :--- | :--- |
| **V1: Unified Mobile-First Interface** | A single, responsive interface for both operators and regulators, optimized for tablets and mobile phones. | - Mobile-first CSS framework (e.g., Bootstrap, Tailwind). |
| **V1: System At-a-Glance** | A dashboard view of a water system's key data points, including contact information, recent violations, and sample results. | - This will be a more detailed version of the public "scorecard," with access to the raw data. |
| **V2: Violation & Compliance Tracker** | A tool to track the status of open violations and upcoming compliance deadlines. | - Filter `SDWA_VIOLATIONS_ENFORCEMENT.csv` by `PWSID` and `VIOLATION_STATUS`. <br> - Use `SDWA_EVENTS_MILESTONES.csv` to populate a compliance calendar. |
| **V3: Site Visit & Reporting Tools** | A digital checklist for regulators to use during site visits, and a simple interface for operators to submit compliance documents. | - File storage solution (e.g., S3). <br> - Offline storage capabilities (e.g., Service Workers) for regulators in the field. |
