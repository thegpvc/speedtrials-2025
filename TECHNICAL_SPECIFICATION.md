# Technical Specification: Georgia Public Trust & Compliance Platform

## 1.0 Introduction

This document outlines the technical specification for the Georgia Public Trust & Compliance Platform, a project designed to modernize the state's public drinking water data infrastructure. The platform will serve three primary user personas: the Public, Water System Operators, and Regulators.

The primary goal of this project is to build a trusted, transparent, and user-centric platform that empowers all stakeholders with clear, contextual, and actionable information about Georgia's drinking water quality.

This document is intended to be a comprehensive guide for a team of AI and human engineers to implement the platform.

## 2.0 System Architecture

The platform will be a modern, full-stack web application with a clear separation between the frontend and backend.

*   **Frontend:** A Next.js (React) application written in TypeScript. This will provide a fast, modern, and SEO-friendly user experience. We will use a component library like ShadCN/UI for the UI components, which will allow for rapid development and a consistent design aesthetic.
*   **Backend:** A Node.js application written in TypeScript, using the Express.js framework. This will provide a robust and scalable foundation for our API.
*   **Database:** A PostgreSQL database to store and manage the application's data. We will use Prisma as our ORM to simplify database interactions and ensure type safety.

## 3.0 Data Schema

The following data models will be implemented in the PostgreSQL database.

### **`WaterSystem`**

Represents a public water system in Georgia.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `id` | `SERIAL PRIMARY KEY` | Unique identifier for the water system. |
| `pwsid` | `VARCHAR(255) UNIQUE NOT NULL` | Public Water System Identifier (e.g., "GA0010000"). |
| `name` | `VARCHAR(255) NOT NULL` | The official name of the water system. |
| `county` | `VARCHAR(255)` | The primary county served by the water system. |
| `populationServed` | `INTEGER` | The number of people served by the water system. |
| `serviceConnections` | `INTEGER` | The number of service connections for the water system. |
| `primarySource` | `VARCHAR(255)` | The primary source of water (e.g., "GroundWater"). |

### **`Violation`**

Represents a violation of a drinking water standard.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `id` | `SERIAL PRIMARY KEY` | Unique identifier for the violation. |
| `pwsid` | `VARCHAR(255) NOT NULL REFERENCES WaterSystem(pwsid)` | The PWSID of the water system that committed the violation. |
| `violationId` | `VARCHAR(255) UNIQUE NOT NULL` | The official identifier for the violation. |
| `compliancePeriodBegin` | `DATE NOT NULL` | The start date of the compliance period for the violation. |
| `compliancePeriodEnd` | `DATE NOT NULL` | The end date of the compliance period for the violation. |
| `violationCode` | `VARCHAR(255) NOT NULL` | The code for the type of violation. |
| `isHealthBased` | `BOOLEAN NOT NULL` | Whether the violation is health-based. |
| `contaminantCode` | `VARCHAR(255)` | The code for the contaminant associated with the violation. |

### **`LCRSample`**

Represents a Lead and Copper Rule sample.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `id` | `SERIAL PRIMARY KEY` | Unique identifier for the sample. |
| `pwsid` | `VARCHAR(255) NOT NULL REFERENCES WaterSystem(pwsid)` | The PWSID of the water system where the sample was taken. |
| `sampleId` | `VARCHAR(255) UNIQUE NOT NULL` | The official identifier for the sample. |
| `samplingEndDate` | `DATE NOT NULL` | The end date of the sampling period. |
| `contaminantCode` | `VARCHAR(255) NOT NULL` | The code for the contaminant (e.g., "PB90" for Lead). |
| `sampleMeasure` | `DECIMAL NOT NULL` | The measured value of the contaminant. |
| `unitOfMeasure` | `VARCHAR(255) NOT NULL` | The unit of measure for the sample (e.g., "mg/L"). |

### **`MCL`**

Represents the Maximum Contaminant Level for a given contaminant, based on the `EPA_MCLS.csv` file.

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `id` | `SERIAL PRIMARY KEY` | Unique identifier for the MCL. |
| `contaminant` | `VARCHAR(255) UNIQUE NOT NULL` | The name of the contaminant. |
| `mclg` | `VARCHAR(255)` | The Maximum Contaminant Level Goal. |
| `mcl` | `VARCHAR(255) NOT NULL` | The Maximum Contaminant Level. |
| `healthEffects` | `TEXT` | A description of the potential health effects of the contaminant. |
| `source` | `TEXT` | The common sources of the contaminant in drinking water. |

## 4.0 Backend API

The backend will expose a RESTful API with the following endpoints:

### **`GET /api/v1/systems`**

*   **Description:** Search for water systems by address.
*   **Query Parameters:**
    *   `address` (string, required): The address to search for.
*   **Response:**
    *   `200 OK`: An array of `WaterSystem` objects that match the search query.
    *   `400 Bad Request`: If the `address` parameter is missing.

### **`GET /api/v1/systems/:pwsid/scorecard`**

*   **Description:** Get the "water scorecard" for a specific water system.
*   **Path Parameters:**
    *   `pwsid` (string, required): The PWSID of the water system.
*   **Response:**
    *   `200 OK`: A JSON object containing the scorecard data, including the overall score (Green, Yellow, or Red), a summary sentence, and the number of recent violations.
    *   `404 Not Found`: If no water system with the given `pwsid` is found.

### **`GET /api/v1/systems/:pwsid/details`**

*   **Description:** Get detailed information for a specific water system, including contaminant data and violation history.
*   **Path Parameters:**
    *   `pwsid` (string, required): The PWSID of the water system.
*   **Response:**
    *   `200 OK`: A JSON object containing the detailed water system data.
    *   `404 Not Found`: If no water system with the given `pwsid` is found.

## 5.0 Frontend Implementation

The frontend will be built with Next.js and will consist of the following pages and components:

### **Pages**

*   **`pages/index.tsx`:** The landing page, which will feature the address search bar.
*   **`pages/system/[pwsid].tsx`:** The main results page, which will display the map and scorecard.

### **Components**

*   **`components/AddressSearch.tsx`:** A reusable search bar component with real-time address suggestions.
*   **`components/WaterSystemMap.tsx`:** An interactive map component that displays water system boundaries and scorecards.
*   **`components/Scorecard.tsx`:** A component to display the water quality scorecard.
*   **`components/ContaminantDetails.tsx`:** A component to display the detailed contaminant data.
*   **`components/ViolationHistory.tsx`:** A component to display the violation history timeline.

## 6.0 Deployment & Operations

*   **Deployment:**
    *   The frontend will be deployed to Vercel for a seamless and scalable hosting experience.
    *   The backend and database will be deployed to a cloud provider like AWS or Heroku.
*   **Operations:**
    *   **Logging:** We will use a logging service like Pino to capture and analyze application logs.
    *   **Monitoring:** We will use a monitoring service like Sentry to track application performance and errors.
    *   **CI/CD:** We will set up a CI/CD pipeline using GitHub Actions to automate testing and deployment.
