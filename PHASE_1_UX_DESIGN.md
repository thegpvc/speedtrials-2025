# Phase 1 UI/UX Design Spec: The Public Trust Platform

This document details the UI/UX design for the public-facing MVP of the Georgia Public Trust & Compliance Platform. The goal is to create an experience that is simple, trustworthy, and empowering for the average citizen.

## 1. Core Philosophy & Design Principles

*   **Clarity Over Comprehensiveness:** The primary goal is to answer the user's core question—"Is my water safe?"—as quickly and clearly as possible. Detailed data is secondary to a clear, immediate answer.
*   **Build Trust Through Simplicity:** A clean, modern, and intuitive interface, free of government jargon and complex forms, is essential for building trust. The design should feel more like a consumer-grade application (e.g., Airbnb, Zillow) than a government portal.
*   **Empowerment Through Action:** We don't want to just inform users; we want to empower them. The user journey must conclude with clear, actionable steps a user can take to protect their family.

## 2. Inspiration & Visual Benchmarks

Our design will be heavily influenced by best-in-class consumer applications that excel at presenting complex, location-based data in a simple, intuitive way. A curated list of these references can be found in `UI_UX_REFERENCES.md`.

## 3. The User Journey: A Step-by-Step Walkthrough

### **Step 1: The Landing Page**

The user arrives on a page that is clean, modern, and focused on a single call to action.

*   **Headline:** "Is your water safe to drink?"
*   **Sub-headline:** "Get the latest water quality report for your address."
*   **The Search Bar:** A single, prominent search bar is the central focus of the page. It will say "Enter your address..."
*   **Visuals:** A clean, abstract background image of water or a map of Georgia. No clutter.

**Textual Wireframe:**

```
+----------------------------------------------------------------------+
| [Logo: Georgia EPD]                                                  |
+----------------------------------------------------------------------+
|                                                                      |
|                  Is your water safe to drink?                        |
|        Get the latest water quality report for your address.         |
|                                                                      |
|      +----------------------------------------------------------+    |
|      | [Icon: Magnifying Glass] Enter your address...           |    |
|      +----------------------------------------------------------+    |
|                                                                      |
|                                                                      |
+----------------------------------------------------------------------+
```

### **Step 2: The Search Experience**

As the user types their address, we will use a "fully automatic address lookup" service to provide real-time suggestions.

*   **Interaction:** As the user types, a dropdown will appear with suggested addresses.
*   **Benefit:** This minimizes user effort and reduces the risk of typos or incorrect addresses.

### **Step 3: The Results Page (Map & Scorecard)**

Once the user selects an address, they are taken to the main results page, which is divided into two panels.

*   **Left Panel: The Water Quality Scorecard**
    *   This is the most critical component of the UI. It must be immediately understandable.
    *   **Header:** The name of the user's water system (e.g., "City of Atlanta Water System").
    *   **The Score:** A large, prominent visual indicator of the water quality. This will be a color-coded circle or shield icon:
        *   **[GREEN] Safe:** No recent violations and all detected contaminants are well below legal limits.
        *   **[YELLOW] Use Caution:** No recent violations, but some contaminants are approaching legal limits.
        *   **[RED] Action Required:** The system has recent violations or contaminants that exceed legal limits.
    *   **The Summary:** A one-sentence, plain-language summary of the score (e.g., "Your water meets all federal and state standards.").
    *   **The "Drill-Down" Button:** A clear, prominent button that says "Learn More & See Details".

*   **Right Panel: The Interactive Map**
    *   The map will show the user's approximate location and the boundaries of their water system.
    *   The water system's service area will be shaded with the corresponding color from the scorecard (Green, Yellow, or Red).
    *   Users can click on other water systems on the map to see their scorecards.

**Textual Wireframe:**

```
+----------------------------------------------------------------------+
| [Logo] [Search Bar: User's Address]                                  |
+----------------------------------------------------------------------+
|                                                                      |
|  +-------------------------+  +------------------------------------+ |
|  |                         |  |                                    | |
|  |  City of Atlanta        |  |                                    | |
|  |  Water System           |  |                                    | |
|  |                         |  |                                    | |
|  |      [GREEN CIRCLE]     |  |      /-------------------\         | |
|  |                         |  |      |       MAP         |         | |
|  |  Your water meets all   |  |      |                   |         | |
|  |  federal and state      |  |      |      [PIN]        |         | |
|  |  standards.             |  |      |                   |         | |
|  |                         |  |      \-------------------/         | |
|  |  [ Button: Learn More ] |  |                                    | |
|  |                         |  |                                    | |
|  +-------------------------+  +------------------------------------+ |
|                                                                      |
+----------------------------------------------------------------------+
```

### **Step 4: The "Drill-Down"**

When the user clicks "Learn More," the left panel expands to show more detailed information.

*   **Contaminant Details:**
    *   A list of all contaminants tested for in the user's water.
    *   For each contaminant, we will show:
        *   The name of the contaminant.
        *   The level detected in the user's water.
        *   The EPA's legal limit (MCL).
        *   A simple visual comparison (e.g., a horizontal bar chart showing the detected level relative to the MCL).
        *   A plain-language explanation of the contaminant and its potential health effects.
*   **Violation History:**
    *   A simple timeline of any violations in the last 5 years.
    *   Each violation will have a clear, plain-language explanation.

### **Step 5: Actionable Guidance**

At the bottom of the "Drill-Down" section, there will be a clear call to action.

*   **Headline:** "How to Protect Yourself"
*   **Content:** A link to a page with a simple guide to common water filters and other actions users can take to reduce their exposure to contaminants. This will be based on the EWG's model.

## 4. Component Library

*   **Search Bar:** A single, full-width search bar with real-time address suggestions.
*   **Map:** An interactive map with custom-styled markers and service area overlays.
*   **Scorecard:** A modular component that can display the water system name, a color-coded score, a summary sentence, and a "Learn More" button.
*   **Contaminant Card:** A card component that displays the details for a single contaminant (name, level, MCL, explanation).
*   **Violation Timeline:** A vertical timeline component that displays a list of violations.
*   **Buttons:** Clean, modern buttons with clear calls to action.
*   **Typography:** A clean, readable sans-serif font (e.g., Inter, Lato).
