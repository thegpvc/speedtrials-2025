# Gemini initial planning convo

Hey, okay, so I'm currently at this hackathon in San Francisco. Basically what's going on is it's a speed trials or speed coding challenge in which one person per team (or one human per team) is allowed, and you're meant to take advantage of AI coding tools and similar in order to actually get shit done as fast as possible. That's really the idea.

What I am going to do is I'm looking for your help breaking down the remaining, let's say two, two and a half hours into the optimal way to use the time. I imagine it's going to look like a structure similar to using the first X amount of time as research, then scaffolding out what we actually want to do, imagining the user experience, making sure that we thoroughly understand the problem. I think a lot of this is going to be data model and problem space.

So I'm going to switch microphones here. I basically want you to help me do the initial thinking and scaffolding out, plan out the research that we'll need to do. I'm looking to do something where I'm not really too concerned about winning this thing, but it's more along the lines of doing stuff in an interesting way, I think. Taking advantage of some of the newer tools, like Worktrees approaches, Gemini CLI, etc. That's more what I care about.

But help me kick this thing off.

Show thinking
Of course. Let's get this kicked off. The goal is an interesting project that leverages modern tools, not just winning. Here’s a breakdown of how to structure the next 2.5 hours for maximum learning and an impressive result.

This plan is designed to front-load the critical thinking, ensuring that when you start coding, you're executing a clear vision.

Phase 1: Ideation & Scoping (First 20 Minutes)
The goal here is to move from a vague idea to a concrete, achievable plan. Be ruthless about cutting scope.

(5 mins) High-Level Brainstorming:

Think about a simple problem you can solve by connecting two distinct things with AI.

Idea Spark: How about a "Git Command Explainer"? You feed it a complex Git command, and it gives you a simple, human-readable explanation and an example. This plays into your interest in tools like Git Worktrees.

Action: Decide on one simple idea. For this plan, we'll use the Git Command Explainer concept.

(15 mins) Define the Core Problem & MVP:

Problem Space: Developers (especially juniors) are often confused by complex Git commands found on Stack Overflow. They need a quick, safe way to understand what a command does before executing it.

User Experience (UX) Flow:

A user sees a single, clean webpage with one text input box and a "Submit" button.

They paste a Git command (e.g., git rebase -i HEAD~5) into the box.

They hit submit.

The page displays a clear, simple explanation of the command, what each part does, and a potential risk or use case.

Minimum Viable Product (MVP): A single HTML page with a form that makes a backend API call. The backend takes the command string, passes it to an LLM via an API, and returns the explanation. That's it. No user accounts, no history, no fancy UI.

Phase 2: Data Modeling & Architecture (Next 30 Minutes)
This is where you solidify the "how." A solid data model, even a simple one, makes coding much faster.

(15 mins) Focused Research & Tooling:

AI Tool: You'll be using an LLM. Your main "research" is to decide on the prompt. How will you ask the AI to generate the explanation?

Prompt Engineering (Draft 1):

As an expert Git instructor, deconstruct the following Git command for a beginner. Explain each component (the command, sub-command, flags, and arguments) in simple terms. Provide a 'Use Case' and a 'Potential Risk'. Format the output as clean HTML.

Command: "{user_command}"
Tech Stack: Let's go with a Python backend (Flask or FastAPI) and plain HTML/CSS for the front end. It's fast and simple.

(15 mins) Data Modeling:

Since this is a simple app, your "data model" isn't a database schema; it's the structure of the data flowing through your system.

API Request (Client -> Server):

JSON

{
  "command": "git rebase -i HEAD~5"
}
API Response (Server -> Client):

JSON

{
  "original_command": "git rebase -i HEAD~5",
  "explanation_html": "<div><h3>Command: <code>git rebase</code></h3><p>...</p><h3>Flag: <code>-i</code></h3><p>...</p></div>"
}
This simple structure is all you need. You've defined the contract between your front end and back end.

Phase 3: Scaffolding with Modern Tools (Next 40 Minutes)
Now, you set up your workspace and generate the boilerplate. This is where you leverage the tools you wanted to explore.

(10 mins) Environment & Git Worktrees Setup:

Create your project directory: mkdir git-explainer && cd git-explainer

Initialize Git: git init

Create your main branch and make an initial commit: git checkout -b main && touch README.md && git add . && git commit -m "Initial commit"

Use Git Worktrees: Instead of switching branches, you'll have two working directories.

Your main branch is in the current directory.

Set up a dev worktree: git worktree add ../git-explainer-dev dev. Now you have a separate folder for development, keeping main clean. You can code in git-explainer-dev.

(30 mins) AI-Powered Code Generation (Gemini CLI):

Now, use the Gemini CLI to generate your starter files. You can do this right from your terminal.

Generate Backend (Flask):

Bash

gemini prompt "Generate a simple Python Flask application in a single file named app.py. It should have one POST endpoint at '/explain' that accepts a JSON object with a 'command' key. For now, just have it return a dummy JSON response." > app.py
Generate Frontend (HTML):

Bash

gemini prompt "Generate a basic index.html file with Bootstrap 5 CDN links. It should have a clean container with a title 'Git Command Explainer', a text area, and a button. Use JavaScript's fetch API to POST the content of the text area to the '/explain' endpoint and display the response." > templates/index.html
You now have functional, albeit disconnected, frontend and backend skeletons without writing much code yourself.

Phase 4 & 5: Implementation & Polish (Remaining 60 Minutes)
This is the final push. Connect the pieces and make it work end-to-end.

(45 mins) Core Logic Implementation:

API Integration: In app.py, import the Google AI library.

Function Stub: Write the function that takes the command string and sends it to the Gemini API using the prompt you engineered earlier.

Connect the Dots: Wire this function into your /explain endpoint. The endpoint should now:

Receive the command from the frontend.

Call the Gemini API.

Return the AI-generated HTML explanation.

Frontend Logic: In index.html, make sure your JavaScript correctly takes the HTML from the API response and injects it into a <div> on the page.

(15 mins) Final Touches:

Add some basic styling.

Ensure the output from the AI looks clean. You might need to tweak your prompt to improve the HTML formatting.

Write a one-sentence description in your README.md.

By following this structure, you focus your energy on the most valuable parts: planning, architecture, and leveraging advanced tools to accelerate development. Good luck!

Okay, cool. So what I want you to do in order to accomplish the above is before you actually give me a plan on how to break down the time, I want you to go traverse the data set—sort of make sure that you get an understanding of what's available to us. Make sure you understand the problem space.

I'm going to go find the RFP for the state of Georgia that actually is related to this thing. If it's not already linked in the repo, I don't think it is. Let's look here.

Basically, what I want you to do is I want you to go—Georgia's current offering. Let's go hardcore research mode. So I want you to go take advantage of any tool and every tool that you have available to you. Take a look at the repo, the data, the reference thing.

Oh lord, this is absolutely horrible. Definitely use playwright to go get a screenshot of this GA drinking water net site.

Let me go try to find the actual RFP. Dispensers drinking water viewer open 6/8, close 17. I feel like it's linked to the source documents word doc. Oh god, macros—why macros? Okay, this is all info. Can I export this? I don't even know what to export. Nice little word lord pdf. Let me try that.

It's a .doc, not even .docx. Lord. I don't understand what the macros are. That's kind of sus. Nice. Hey, beautiful. Do more caps for something I'll change. What the hell is that? Unnecessary wasted tokens. Much better to read.

I've been hiding my screen still this whole time. Oh, Lord, sorry. Awkward. Okay, so I was just in the middle of downloading the RFP doc and let me just read through this. Oh, RFI. Required functionality. Okay. Public can view data for chosen water system.

Oh, this Willow Voice thing is so awesome. Then I'll lose that and you can kind of use it wherever and just paste it afterwards. I think that's really nice.

Alright, so we got that. Let's go here. I'm going to stop trying to do these multiple times to repeat work.

Okay, challenge repo. What the hell did my nana? I guess I can't do that. Is there a comment on these things? Last one. Yeah, no, they're accepted.

Okay, and then let's see. What was the last bit that I wanted to do? The screenshot in WebP. And then here so that it actually is not putting the repo because I do want to upload the thing.

Let's go in notes. Can I actually do this in notes? I think so. I'll just do that. Hallelujah again. There are the keys again. Lord. All right, screw it. What do I have to replace? Fire crawl and perplexity later.

All right, that's fine. I'm just replacing before sharing the recording. I think I just do this one. No, that's a temporary one. I didn't clear this. Yeah, I'm just going to get rid of my Serena Mindy's. I don't need that.

It seems like Mae's calling me. Hey, mate. Oh, yeah. Cool. I think I can let you in. Let me see. Oh, yeah. Oh, beautiful. Yeah, just come up. Yeah, and then if you come inside, go to your right and then go down towards the far wall. And I'm in one of those side rooms—probably third one. I think behind the glass. Yeah, spot to hang out. All right, see you in a bit. Bye.

So I'm gonna kick this thing off because I probably only have two hours to run research execute this, but I've tended to find that the upfront research is a lot better and keeping everything on track.

So number one thing is trying to make it easier. The Georgia residents understand the safety of their drinking water, operators, human information on their system. That's a second profile. And then third profile field kit. Okay. So there's three user profiles to build for. That's kind of interesting.

Here's the question: Do I need information on their system? Track notices from regulators. It doesn't say that. Interesting. It doesn't say that there has to be things that the public can't see here. It would be pretty helpful if I could just avoid having to do auth whatsoever. I'm not allowed to help, right? We can talk to each other, so you're not allowed to actually code anything with me, but I imagine it would be fine.

Oh, if you do auth in public, are you getting any auth? Yeah, I was more thinking about the operators and regulators. Is that like one of those things where you have to do government-level auth? I think it would be kind of cool to frame it as, hey Georgia, the public really loves when government is open and this is something that the government is embracing. Take a look at the way that, whether you like it or not, the Doge team is handling things, trying to increase transparency.

So we've given you a public-facing thing that makes it convenient for the public and kind of spoon feeds the information for them. An operator-facing one that gives you a level of granularity. And a regulator one, which lets them go as deep in the weeds as they want to. And if the public wants to access those things as well, totally fine too.

Yeah, okay, I like that. Look through the data directory, understand structures and patterns. Yeah, I'm not going to do that. I'm going to let Claude and Gemini do that. Ingest the raw data into a clean query-able database. Are you just going to experiment? Basically, I was like fucking around with the recording for like an hour and a half. And then setting up some tools and project stuff.

Data directory, structuring patterns, queryable database, augments of any additional data you need, geographic data mapping, Georgia's current operating out of the 2000s. Here's the website, by the way. This thing is crazy. Drinking water site is this one. Look at this thing. You have to type in water system number, name, principal, county, serve, like Jesus. There's zero chance anyone knows any of this.

Yeah. I think there's some cool visualizations you could do. Apparently they ask a lot. That's the interesting part. Like, is it getting better or worse? Well, like, is my water drinkable seems to be the key user for some of the questions. Oh, for sure. But you have to sell them if they want to, like, dig into it more than they can. There's a review. Search. Oh my god, that's the search. It's just a spreadsheet. jesus christ lol

I was thinking the Doge leaderboard—how it's like the most wasteful government programs are at the top. I honestly don't have an idea of a leaderboard with rankings because then it becomes more of like a shareable thing of "oh shit you guys," but then I guess the next thing would be like, okay water is bad but like there might be some other things to talk about.

Yeah, I think... I wonder what the actual consumer confidence data... It does not currently include updated CCR requirements that are dictated by LEED and Copper Rural. Okay, interesting. So you can generate a report. Schedule, welcome. No, okay. What? Okay, so imagine you have... Oh, on the

Wait, say that one more time. So it's like, hey, I'm at the location where I'm curious about drinking water. It's like a game where you spin the water bottle and then it either points to you yes or no. That's a UX thing.

Somehow I feel like the state of Georgia would be very excited about you implying it's a gamble as to whether or not your water is drinkable. The high school where you're like, "Yeah, but what does this have to do with that?" I just think it's funny, right? It's quirky. You should have a quirky UI around it. I think quirky could be good. Maybe give it a character.

Okay, let me focus for a sec. So I want to get glossary directly into the environment here. I think that'd be good. Ugh. Yeah, I don't need it. I don't need it. Hopefully it never has to.

Alright, I can just use firecrawl. Hopefully you never wait, what? Because we'll never have this many. Okay, firecrawl, markdown, copy, used. Why not dog's class job? Why are you using firecrawl? Because it's better than yours. Yeah, they did a really, really good job. Okay, no way. For now, anyway. Why is that at the top? Oh, it's a flosso.

Okay. I did county map. If I click on this, then you can click on Atlanta. Status A. What is status I? Interesting. Microbial samples. Interesting. All right.

—

**State of Georgia**

**State Entity: Department of Natural Resources - EPD**

**Electronic Request for Information (“eRFI”)**

**Event Name: Drinking Water Viewer / RECAP Report**

**eRFI (Event) Number: 46200-DNR0000804**

1. **Introduction**

1. **Purpose of Solicitation**

This electronic Request for Information (“eRFI”) is being issued to solicit information from interested suppliers with respect to Drinking Water Viewer / RECAP Report for the Department of Natural Resources – Environmental Protection Division (EPD) (hereinafter, “the State Entity”) as further described in this eRFI. The State Entity will use the information generated by this eRFI in conjunction with other information available to the State Entity to determine the solution that it is in the best interests of the State Entity to fulfill this need.

- 1. **Overview of the eRFI Process**

The objective of the eRFI is to gather information to assist the State Entity in its consideration of available resources/methods to fulfill the need/goal identified above. The eRFI method is not a competitive solicitation method and, as a result, does not satisfy the requirement for competitive bidding. The eRFI method is no more than an information gathering tool and such information gathered may or may not be used by the State Entity to develop a competitive solicitation. Suppliers are not required to respond to an eRFI and a supplier’s failure to respond to an eRFI will not prohibit the supplier’s participation in any competitive solicitation that may result from the eRFI. However, suppliers are strongly encouraged to respond to eRFIs as this is a great way to ensure the State Entity is aware of the suppliers’ available goods and services.

- 1. **Schedule of Events**

The schedule of events set out herein represents the State Entity’s best estimate of the schedule that will be followed. However, delays to the procurement process may occur which may necessitate adjustments to the proposed schedule. If a component of this schedule, such as the close date, is delayed, the rest of the schedule may be shifted as appropriate. Any changes to the dates up to the closing date of the eRFI will be publicly posted prior to the closing date of this eRFI. After the close of the eRFI, the State Entity reserves the right to adjust the remainder of the proposed dates on an as needed basis with or without notice.

| **Description** | **Date** | **Time** |

| --- | --- | --- |

| Release of eRFI | As Published on the Georgia Procurement Registry (“GPR”) | N/A |

| Written Questions | 06/27/2025 | 5:00 p.m. ET |

| Responses to Written Questions | 07/02/2025 | 5:00 p.m. ET |

| Deadline for Submitting Responses | As Published on the GPR | See GPR |

- 1. **Official Issuing Officer (Buyer)**

**Rhonda Henslee**

**<Rhonda.Henslee@dnr.ga.gov>**

- 1. **Definition of Terms**

Please review the following terms:

Supplier(s) – companies desiring to do business with the State of Georgia.

State Entity – the governmental entity identified in Section 1.1 “Purpose of Solicitation” of this eRFI.

COTS – Commercial-off-the-shelf

DWP – Drinking Water Program

DWV – Drinking Water Viewer

EPD – Environmental Protection Division

EPD-IT – Environmental Protection Division Information Technology

PWS – Public Water Supply

QA/QC – Quality Analyze/Quality Control

RECAP – Report Evaluation Compliance and Processing

RFI – Request for Information

SDWA – Safe Drinking Water

SDWIS – Safe Drinking Water Information System

Any special terms or words which are not identified in this State Entity eRFI Document may be identified separately in one or more attachments to the eRFI. Please download, save and carefully review all documents in accordance with the instructions provided in Section 2 “Instructions to Suppliers” of this eRFI.

1. **Instructions to Suppliers**

By submitting a response to the eRFI, the supplier is acknowledging that the supplier:

1. Has read the information and instructions,

2. Agrees to comply with the information and instructions contained herein.

1. **General Information and Instructions**

**2.1.1. Team Georgia Marketplace™ Registration System**

The Department of Administrative Services (“DOAS”) requires all companies and/or individuals interested in conducting business with the State of Georgia to register in the State’s web-based registration system, through Team Georgia Marketplace™. Registration is free and enables the registering company to gain access to certain information, services and/or materials maintained in Team Georgia Marketplace™ at no charge to the registering company. All registering companies must agree to be bound by the applicable terms and conditions governing the supplier’s use of Team Georgia Marketplace™. In the event DOAS elects to offer certain optional or premium services to registered companies on a fee basis, the registered company will be given the opportunity to either accept or reject the service before incurring any costs and still maintain its registration. Companies may register at <https://fscm.teamworks.georgia.gov/psc/supp/SUPPLIER/ERP/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL?&>

**2.1.2. Submitting Questions**

All questions concerning this eRFI must be submitted in writing via email to the Issuing Officer identified in Section 1.4 “Issuing Officer” of this eRFI. Do not use the comments section within the sourcing tool to submit questions to the issuing officer.

**2.1.3. State’s Right to Amend and/or Cancel the eRFI**

The State Entity reserves the right to amend this eRFI. Any revisions must be made in writing prior to the eRFI closing date and time. By submitting a response, the supplier shall be deemed to have accepted all terms and agreed to all requirements of the eRFI (including any revisions/additions made in writing prior to the close of the eRFI whether or not such revision occurred prior to the time the supplier submitted its response) unless expressly stated otherwise in the supplier’s response. THEREFORE, EACH SUPPLIER IS INDIVIDUALLY RESPONSIBLE FOR REVIEWING THE REVISED eRFI AND MAKING ANY NECESSARY OR APPROPRIATE CHANGES AND/OR ADDITIONS TO THE SUPPLIER’S RESPONSE PRIOR TO THE CLOSE OF THE eRFI. Suppliers are encouraged to frequently check the eRFI for additional information. Finally, the State Entity reserves the right to cancel this eRFI at any time.

**2.1.4. Costs for Preparing Response**

Each response should be prepared simply and economically, avoiding the use of elaborate promotional materials beyond those sufficient to provide a complete presentation. The cost for developing the response and participating in this eRFI process is the sole responsibility of the supplier. The State will not provide reimbursement for such costs.

**2.1.5. ADA Guidelines**

The State of Georgia adheres to the guidelines set forth in the Americans with Disabilities Act. Suppliers should contact the Issuing Officer at least one day in advance if they require special arrangements when attending the Informational Conference (if any). The Georgia Relay Center at 1-800-255-0056 (TDD Only) or 1-800-255-0135 (Voice) will relay messages, in strict confidence, for the speech and hearing impaired.

**2.1.6. Public Access to Procurement Records**

Solicitation opportunities will be publicly advertised as required by law and the provisions of the Georgia Procurement Manual. The State Entity is allowed to assess a reasonable charge to defray the cost of reproducing documents. A state employee should be present during the time of onsite inspection of documents. PLEASE NOTE: Even though information (financial or other information) submitted by a supplier may be marked as "confidential", "proprietary", etc., the State will make its own determination regarding what information may or may not be withheld from disclosure.

**2.1.7. Registered Lobbyists**

By submitting a response to this eRFI, the supplier hereby certifies that the supplier and its lobbyists are in compliance with the Lobbyist Registration Requirements in accordance with the _Georgia Procurement Manual_.

- 1. **Submittal Instructions**

**Submittal Instructions for Team Georgia Marketplace™**

Listed below are key action items related to this eRFI. The Schedule of Events in Section 1.3 identifies the dates and time for these key action items. This portion of the eRFI provides high-level instructions regarding the process for reviewing the eRFI and preparing and submitting a response to the eRFI. Suppliers are required to access, print and utilize the training materials identified in Section 2.2.1 of this eRFI to ensure the supplier successfully submits a response to this eRFI.

- - 1. **eRFI Released – Team Georgia Marketplace™**

The release of the eRFI is formally communicated through the posting of this eRFI as an event in Team Georgia Marketplace™ and by a public announcement posted to the Georgia Procurement Registry, which is accessible online as follows: <http://ssl.doas.state.ga.us/PRSapp/PR_index.jsp>

This eRFI is being conducted through Team Georgia Marketplace™, an online, electronic tool, which allows an individual to register, logon, select answers and type text in response to questions, and upload any necessary documents. Team Georgia Marketplace™ permits an individual to build and save a response over time until the registered user is ready to submit the completed response. Each supplier MUST carefully review the instructions and training information from the following link for a comprehensive overview of the functionality of Team Georgia Marketplace™:

<http://doas.ga.gov/state-purchasing/purchasing-education-and-training/supplier-training>

- - 1. **eRFI Review**

The eRFI (or “Event”) consists of the following: this document, entitled “The State Entity eRFI Document”, any and all information included in the Event, as posted online on Team Georgia Marketplace™, including questions and instructions, and any and all documents provided by the State Entity as attachments to the Event or links contained within the Event or its attached documents.

Please carefully review all information contained in the Event, including all documents available as attachments or available through links. Any difficulty accessing the Event or opening provided links or documents should be reported immediately to the Issuing Officer (See Section 1.4) and/or the Help Desk (Section 2.2.8). Attached documents may be found as follows:

1. First, the State Entity will provide documents at the “header” level of the Event. Please select “View/Add General Comments & Attachments”, which appears at the top of the screen of the Event under the “Event Details” Section. Next, by selecting “View Event Attachments”, the supplier may open and save all of the available documents. In this location, the supplier is most likely to find this document as well as any worksheets. Please thoroughly review all provided Event Attachments.

2. Second, the State Entity may also provide documents in the section of the Event entitled “eRFI Questions”. To the right of each question appearing under the eRFI Questions section, the Event contains an icon (appears as a bubble with text). By selecting this icon, the supplier will navigate to a new page of the Event. On this new page the supplier can locate attached documents.

Please thoroughly review all provided attachments. For additional information regarding the use of Team Georgia Marketplace™, please utilize the online resources provided in Section 2.2.1 of this eRFI.

- - 1. **Preparing a Response**

As noted earlier, Team Georgia Marketplace™ allows the supplier to answer questions by entering text and numeric responses. In addition, as noted in Section 2.2.4 “Uploading Forms”, the supplier may also provide information by uploading electronic files. When preparing a response, the supplier must consider the following instructions:

1. The supplier must ensure its response is accurate and readily understandable.

2. The supplier must label any and all uploaded files using the corresponding section numbers of the eRFI or any other logical name so that the State Entity can easily organize and navigate the supplier’s response.

3. The supplier must use commonly accepted software programs to create electronic files. The State Entity has the capability of viewing documents submitted in the following format: Microsoft Word or WordPad, Microsoft Excel, portable document format file, and plain text files with the file extension noted in parentheses (.txt). Unless the eRFI specifically requests the use of another type of software or file format than those listed above, please contact the Issuing Officer prior to utilizing another type of software and/or file format.

4. The supplier must save its response until the supplier is ready to submit its bid. Select the “Save for Later” button at the top of the page under “Event Details” of the Event.

- 1. **Uploading Forms**

Once the supplier is ready to upload electronic files (completed forms or worksheets, product sheets, etc.), please following the directions within the eRFI to upload these documents in the proper location. There are two places to upload completed documents:

1. First, the “View/Add General Comments & Attachments” link contains a place for the supplier to upload all of the documents and worksheets which were provided by the State Entity under the “View Event Attachments” link. Once the supplier has completed the Event Attachments, the supplier can then select “Add New Attachments” to upload the completed documents. The supplier can upload as many documents as necessary in this section of the Event.

2. Second, the supplier can also upload documents by selecting the comment bubble icon, which appears to the right of each eRFI question.

- 1. **Reviewing the Response Prior to Submission**

During the time period allowed for preparing the response, neither DOAS nor the State Entity can view what information or documents are being added by the registered user. In other words, the State Entity cannot know whether the supplier’s response is correct or complete until after the eRFI has closed. Therefore, each supplier is responsible for ensuring all questions have been answered appropriately and that all necessary documents have been uploaded.

- - 1. **Submitting the Completed Response/Bid**

**Once the completed response has been reviewed by the supplier, click the "Submit Bid" button at the top of the page under the “Event Details” section of the Event.** Please note that submission is not instantaneous; therefore, each supplier must **allow ample time for its response to be submitted prior to the deadline**.

- - 1. **Reviewing, Revising or Canceling a Submitted Response**

After the response has been submitted, the supplier may view and/or revise its response by logging into Team Georgia Marketplace™ and selecting the eRFI event number and the “View/Edit” feature for the supplier’s previous response. Please take note of the following:

- 1. REVIEW ONLY. In the event the supplier only wishes to view a submitted response, the supplier may select “View/Edit”. Once the supplier has finished viewing the response, the supplier may simply exit the screen. DO NOT SELECT “Save for Later.” Team Georgia Marketplace™ recognizes any response placed in the “Save for Later” status as a work in progress and withdraws the originally submitted bid. As a result, unless the supplier selects “Submit” prior to the closing date and time, no response will be transmitted to the State Entity.

2. REVIEW AND REVISE. In the event the supplier desires to revise a previously submitted response, the supplier may select “View/Edit” and then revise the response. If the revisions cannot be completed in a single work session, the supplier should save its progress by selecting “Save for Later.” Once revisions are complete, the supplier **MUST** select “Submit” to submit its corrected response. Please permit adequate time to revise and then resubmit the response. Please note submission is not instantaneous and may be affected by several events, such as the supplier temporarily losing a connection to the Internet.

PLEASE USE CAUTION IN DECIDING WHETHER OR NOT TO MAKE REVISIONS. The State will assume no responsibility for a supplier’s inability to correct errors or otherwise make revisions to the submitted response prior to the eRFI end date and time.

3\. WITHDRAW/CANCEL. In the event the supplier desires to revise a previously submitted response, the supplier may select “View/Edit” and then select “Save for Later”. Team Georgia Marketplace recognizes any response placed in the “Save for Later” status as a work in progress and **_withdraws the originally submitted bid_**. As a result, unless the supplier selects “Submit” prior to the closing date and time, no response will be transmitted to the State Entity.

- - 1. **Help Desk Support**

For technical questions related to the use of Team Georgia Marketplace™, suppliers have access to phone support through the DOAS Customer Service Help Desk at 404-657-6000, Monday through Friday 8:00 AM to 5:00 PM excluding State Holidays or any other day state offices are closed such as furlough days or closings in response to inclement weather. Suppliers can also email questions to: [ProcurementHelp@doas.ga.gov](mailto:ProcurementHelp@doas.ga.gov).

**3\. Requested Information**

## Agency Overview

The Environmental Protection Division (EPD) of the Georgia Department of Natural Resources is a state agency charged with protecting Georgia's air, land, and water resources through the authority of state and federal environmental statutes. These laws regulate public and private facilities in the areas of air quality, water quality, hazardous waste, water supply, solid waste, surface mining, underground storage tanks, and others. EPD issues and enforces all state permits in these areas and has full delegation for federal environmental permits except Section 404 (wetland) permits.

## The Opportunity

In the early 1990s, EPA set out to provide important drinking water agencies with an information system that would not only report accurate data to the federal system on a timely basis but would also support the rule implementation activities of primacy agencies so that these agencies would not have to develop an information system on their own. That system, known as the Safe Drinking Water Information System (SDWIS/STATE), needed to be efficient enough to enable compliance determination for a host of growing EPA regulations, and it needed to gain acceptance by addressing the specific needs of a large and varied base of primacy organizations.

&nbsp;

Drinking Water Program (DWP) is looking to implement a new solution to, process, and analyze water-related data from the existing SDWIS to provide comprehensive insights into availability, quality, consumption, and distribution. By integrating with SDWIS, this solution aims to improve decision-making, optimize resources management, and enhance transparency in water-related operations. The Drinking Water Program is taking this opportunity to provide live water system information at your fingertips. Drinking Water Viewer (DWV) will view current SDWIS water system data including sample results, compliance data, and inventory.

## Purpose of Request for Information

The purpose of this Request for Information (RFI) is to explore potential DWV Commercial-Off-The-Shelf (COTS) solutions that will integrate with SDWIS. This integration aims to enhance access to real-time and historical water quality data, improve decision-making capabilities, and ensure compliance with regulatory standards. The drinking water viewer will enable the program and the public to visualize and analyze water quality information efficiently.

## RECAP

Report, Evaluation, Compliance, and Processing (RECAP) is a road map item and not an immediate need.

## Benefits

- RECAP has more advanced functionality than Microsoft Access Databases.

- RECAP’s four add-on features use web services to extract information from databases and present it in useful formats.

- Quickly generate reports and metrics to assist agency staff with compliance determination and keeping water systems in compliance with the Safe Drinking Water Act (SDWA) regulations.

- RECAP can be integrated with other applications to display information.

## Reports

- Generates custom reports, outputs, and letters to help important agencies quickly review water system data and compliance information.

- Letters, reminders, and reports can be sent to water systems to help them remain in compliance with SDWA regulations.

## Dashboard

- Tracks to-do list of tasks that can be marked as completed so managers can see if staff are addressing issues.

- Ensure things don't fall through the cracks and help staff keep up with routine compliance activities.

- Help managers, compliance and enforcement staff focus on using grids, metrics, and graphs on an uncluttered dashboard.

&nbsp;

## System Requirements

The solutions will be reviewed and evaluated based on the following key features:

General System Capabilities

Describe how well the product/solution serves the EPD Drinking Water Program’s needs:

1. User Management

2. Operation Capacity

3. Compliance with Regulatory Requirements and Industry Standards

## Required Functionality

Describe how well the product/solution serves the EPD Drinking Water Program’s needs:

- The public can view data for a chosen water system or search for specific data across many water systems.

- Operators can view information to help them better manage their water system.

- Laboratories can Quality Analyze/Quality Control (QA/QC) data submitted to the important agency and download data needed for electronic sample submissions.

- State and EPA staff can pull up live, detailed information from their phone for meetings, conferences, or on-site visits.

## Accessibility

DWV is a user-friendly, intuitive application designed to enable any user to find drinking water data for their state, including:

- Water System Inventory (e.g., facilities and sampling points)

- Samples

- Violations

- Enforcements

- Schedules & Activities

- Site Visits

- Deficiencies

## Technology Requirements

Describe how well the product/solution serves the overall technological needs:

1. Delivery Method

- Web-based/Hosting (Azure, Amazon Web Services (AWS), or Salesforce)

1. Maintenance and Support

## User Management

This is the core function that controls system access and permissions and covers what users are authorized to do.

- The ability to create new user accounts and remove and/or lock user accounts.

- Create user privileges based on function.

- Control which users have the right to view only / update specified data.

## Operation Capacity

- Two agency users.

- One administration user.

- External users will not need accounts since it is free for public users.

## Data Integration

The new solution uses modern technologies (e.g., web services/APIs) that will be compatible with SDWIS Modernization.

## Supplier Background

Company History and Affiliations:

Office Locations:

Statement of Core Business Competencies:

## Capabilities And Experience

When detailing experience, document experience on at least three and no more than five projects completed no earlier than 2020.

- Capabilities:

- Experience:

- Why you’d be a good fit:

## Software Pricing Model

- Cost Per License

Do you subcontract work to 3<sup>rd</sup> parties? If yes, explain:

## Additional Information

Detail any further information believed to be beneficial in support of this Request for Information review effort.

**4\.** **Additional Information**

The State Entity may, at its discretion, ask one or more suppliers to provide additional information and/or meet with the State Entity to further discuss the supplier’s information.

**5\. List of eRFI Attachments**

The following documents make up this eRFI. Please see Section 2.2.2 “eRFI Review” for instructions about how to access the following documents. Any difficulty locating or accessing the following documents should be immediately reported to the Issuing Officer.

1. State Entity eRFI (this document)

2. Special Term Definitions from Section 1.5 “Definition of Terms” of this eRFI – NOT Applicable

—

## Research

### Existing horrible ugly current site GA is looking to replace

<https://gadrinkingwater.net/DWWPUB/>

### Bid Banana - Drinking Water Viewer / RECAP Report

<https://bidbanana.thebidlab.com/bid/V3T5BeqhF6PnZhyeAJyr>

### GA gov site - already downloaded and converted to markdown as GA_RFP_DOC.md

<https://fscm.teamworks.georgia.gov/psp/supp/SUPPLIER/ERP/c/DX_SRM_MENU.DX_AUC_EVENT_ATTCH.GBL?PORTALPARAM_PTCNAV=DX_AUC_EVENT_ATTCH_GBL&EOPP.SCNode=ERP&EOPP.SCPortal=SUPPLIER&EOPP.SCName=EPAUC_PREPARE_BID&EOPP.SCLabel=Manage%20Events%20and%20Place%20Bids&EOPP.SCPTfname=EPAUC_PREPARE_BID&FolderPath=PORTAL_ROOT_OBJECT.EPAUC_PREPARE_BID.DX_AUC_EVENT_ATTCH_GBL&IsFolder=false&SearchAction=DirectLink&BUSINESS_UNIT=46200&AUC_ID=DNR0000804>

—

# 🏁 Codegen Speed Trials - Challenge Repo

**🚰 What's in our public drinking water? Turn Georgia's cryptic water quality data into something the public, operators, and regulators can actually use.**

American's [top environmental concern](https://news.gallup.com/poll/643850/seven-key-gallup-findings-environment-earth-day.aspx) is pollution in their drinking water. The EPA publishes [national drinking water data](https://www.epa.gov/ground-water-and-drinking-water/safe-drinking-water-information-system-sdwis-federal-reporting), but it's difficult to interpret, especially for the public or under-resourced rural water systems.

To give you a feel for existing solutions, here's the state of Georgia's official drinker water viewer:

<img width="900" alt="Screenshot 2025-06-27 at 8 30 45 PM" src="https://github.com/user-attachments/assets/d8f7c9e9-a146-4a8f-b6c7-fed8d634ca2c" />

**✨ The good news:** the Georgia Environmental Protection Division knows the public deserves better! Three weeks ago, they published a [Request for Information](https://drive.google.com/file/d/13VkRTJhGJcF9FmgrXs-j4PZzI3jepFvq/view?usp=sharing) to overhaul the whole thing.

**✅ Your task:** Set the water data free. Build a product that ingests real-world raw water quality data and empowers the public and water systems operators to interpret and act on it.

## 🗂️ What We're Giving You

In the [data](data/) directory, you'll find a raw export of the public Georgia water system data from SDWIS along with a README packed with helpful context and links. Feel free to augment!

The Georgia RFP wants solutions for three primary stakeholders:

1. **The Public:** Make it easier for Georgia residents to understand the safety of their drinking water. You could help them better understand what violations mean, the health implications of different contaminants, or take action to stay up-to-date on their local water system.

2. **The Operators:** Help water system operators view information on their system, track notices from regulators, and take action on compliance tasks.

3. **The Regulators:** A field kit allowing them to quickly understand the live status of a water system on-the-go on site visits or in meetings. They'll need to drill down into specifics, but high level summaries are helpful too!

## Getting Started

1. **Fork**

- Fork this repository, you'll include a link to your fork in your submission.

3. **Explore:**

- Look through the [data directory](data/) to understand structure and patterns.

- Ingest the raw data into a clean, queryable database.

- Feel free to augment with any additional data you need (e.g. geographic data for mapping)

4. **Create:**

- Take [Georgia's current offering](https://gadrinkingwater.net/DWWPUB/) out of the 2000s.

- You can build for the Public, the Operators, the Regulators (or all three!).

1. **Submit:** Instructions below.

## Implementation Requirements

- **Don't sweat hosting:** You can build the whole thing locally and share a live link via [ngrok tunnel](https://ngrok.com/our-product/secure-tunnels) (or similar) to your localhost:

```shell

brew install ngrok

# If you don't have one, sign up for a free ngrok account at https://ngrok.com

ngrok config add-authtoken <your-ngrok-auth-token>

ngrok http http://localhost:<your-local-server-port>

```

- **BYO stack:** As long as you follow the submission instructions, you can take any approach you want — any libraries, any DB, any interface. We will be rewarding bold swings!

## ⚖️ Judging

Unlike traditional hackathons, the Codegen Speed Trials aren't just about what you build, they're about how you build it. We'll reward participants who take the challenge the furthest, but we're equally excited to celebrate innovative collaborations with AI.

​Projects will be scored across four categories:

1. **Core Delivery:** Does your submission preserve and accurately represent the data provided?

2. **Impact and Relevance:** Does your submission improve on [Georgia's exising solution](https://gadrinkingwater.net/DWWPUB/) for the public, water system operators, regulators (or multiple)?

3. **Ambition and Scope:** Did you take a big, creative swing at the problem? How far beyond the baseline did you dare to go?

4. **Iron Man Score:** Did you make creative use of AI tools and agents to get the challenge done?

We have $1000s in cash and credit prizes to award for winning submissions, and are excited to see what you build!

## 📤 Submission Instructions

**Submissions are due by 5 PM. [Use this link to submit.](https://cerebralvalley.ai/e/codegen-speedtrials-2025/hackathon/submit)**

Include the following with your submission:

1. A public link to your forked Github repo

2. 3. A link to a short (< 2 min) video explaining your submission and the tools + approaches you used to build it. We want to hear details on how you accelerated your work using AI!

3. A link via [ngrok tunnel](https://ngrok.com/our-product/secure-tunnels) (or similar) to your localhost:

**Important:** your tunnel will need to remain accessible throughout the entire judging period, which runs from 5-7P PT.

---

Good luck!

—

Okay. So I just did a bunch more digging above. I have a cloud code instance as well as a Gemini CLI instance up and running in a carbon copy environment, added a couple of notes files and some of the stuff from the original site, the actual RFP file.

One of the things that I'd like for you to do is to effectively help me structure through the best way to spend the remaining hour and a half, two hours. Again, I think putting the most emphasis into the upfront understanding of the problem, getting agent context, making some prep and plan documents tends to work the best in my mind.

There's also some additional research that we can do maybe as a second phase, and then given all of that initial context and understanding of the data set, the existing site, what the state of Georgia probably wants in terms of the value prop here—all that requisite context—then we can kind of shift towards PRD and specking out the user journey, the interface, that sort of thing.

And then I do already have a ShadCN Next.js project set up, and maybe we go neon for the branching effects, something like that. I'm not 100% sure what to do with DB, or maybe your thoughts would be helpful here about SQLite, perhaps. Something that we can easily manage locally kind of makes sense to me.

But very first question to you, I want your help thinking through exactly what you just gave me a draft of, but with less context—give me the optimal structure and use of time, if you will.

I've also included some of the key documents such as the README for the competition, as well as some of the notes that I took and then the reference locations.

Show thinking
Alright, let's do this. You've done the critical groundwork by gathering the assets. Now we need to weaponize that research and structure the next two hours for maximum impact. The goal is a bold, creative swing that showcases modern tools and a deep understanding of the problem.

Given the new context from the RFI and the challenge repo, the initial idea of framing this around government transparency is a home run. We'll build for all three personas but lead with the public-facing one as the "hook."

Here is the optimal structure for your next two hours.

Phase 1: Synthesize & Strategize (First 30 Minutes)
Goal: Transform raw information into a coherent strategy and a defined project scope. This is the most critical phase.

(15 mins) AI-Powered Data & Document Analysis:

Your Task: You have the data files, the RFI, and notes. Don't analyze them manually. Use your AI tools.

Action: Point Gemini/Claude at the data/ directory and the GA_RFP_DOC.md.

Prompts to Use:

"Analyze the files in the data directory. Describe the schema of each file (columns, data types) and identify the key fields that link these files together. What is the primary key for a water system? Summarize the overall data structure."

"Based on the GA_RFP_DOC.md and the challenge README, what are the top 3 functional requirements for each user persona: Public, Operator, and Regulator? Frame them as 'user stories'."

"Cross-reference the data schemas with the RFI requirements. What key information, like 'violations' or 'contaminant levels', seems most critical for building this application?"

(15 mins) Define Core Strategy & Tech Stack:

Your Task: Solidify the "big idea" and make key technical decisions.

Strategy: Frame the project as "Georgia Water Watch: Radical Transparency for Public Health." The idea is that all data is public for all three personas, but the interface is tailored to their needs. This neatly sidesteps the need for complex auth.

Database Choice: Use SQLite. It's perfect for this. It's a single file you can commit to your repo, it's incredibly fast for reads, and you can ingest the CSV data into it in minutes. It requires zero setup and is ideal for a local-first hackathon project.

Tech Stack Confirmation:

Frontend: Next.js + ShadCN (already set up, perfect).

Backend: Next.js API Routes.

Database: SQLite.

Deployment: ngrok tunnel to your localhost.

Phase 2: Product Definition & UX (Next 40 Minutes)
Goal: Go from a high-level strategy to a concrete plan of what you're building, page by page.

(20 mins) Write a "1-Pager" PRD (Project Requirements Document):

Your Task: Create a new file, prd.md, in your repo. This forces clarity. It shouldn't be long, but it should be precise.

Structure:

Vision: A one-sentence summary. (e.g., "A user-friendly portal that makes Georgia's public water quality data accessible, understandable, and actionable for citizens, operators, and regulators.")

User Personas & Stories: Copy the user stories generated by the AI in the previous step.

MVP Scope: Define the one killer feature. I recommend a "Universal Search & System Profile Page." A single search bar on the homepage that lets anyone search by zip code, county, or water system name. The result is a beautiful, easy-to-read profile page for that water system.

The "Wow" Factor: What's the quirky, memorable element? Let's go with a "Water Health Score." A simple A-F letter grade for each water system, calculated based on the number and severity of recent violations. This is shareable and immediately understandable.

(20 mins) Whiteboard the User Journey & UI:

Your Task: Don't touch code yet. Sketch it out. Use a tool like tldraw or just a piece of paper.

Flow to Sketch:

Homepage: Big, bold title. A single, beautiful search bar. Minimalist text.

Search Results: As the user types, show an autocomplete dropdown of matching water systems.

System Profile Page (The Core of the App):

Header: System Name, County, and the big "A-" Water Health Score.

Public View: Simple cards for "Recent Violations," "Contaminants Tested," and a plain-language summary: "Is my water safe to drink?" (generated by an LLM).

Operator/Regulator View: A tabbed interface on the same page. The other tabs could be "Full Compliance History," "Raw Sample Data," "System Inventory." This fulfills the RFI without needing new pages or auth.

Phase 3: Development & Execution (Remaining 50 Minutes)
Goal: Translate your plan into working code as fast as possible.

(20 mins) Data Ingestion & Backend Scaffolding:

Your Task: Get the data into SQLite and create the API endpoint.

Action:

Write a simple Python or Node.js script (ingest.js) to read the CSV files from the data/ directory and load them into a local.db SQLite file.

Use the Gemini CLI to scaffold a Next.js API route (/api/systems/[id].js) that takes a system ID, queries the SQLite database, and returns the system's data as JSON.

(30 mins) Frontend Implementation:

Your Task: Build the UI you sketched.

Action:

Homepage: Use a ShadCN input component for the search bar.

Profile Page: Create the dynamic page [id].js.

Component-Driven Dev: Use the Gemini CLI to generate individual React components based on your sketch: HealthScoreBadge, ViolationCard, DataTable, etc. Prompt it like: "Create a React component using ShadCN's Card component to display a water quality violation with a title, date, and description."

Focus on getting the Public View of the profile page working first. If you have time, add the other tabs.

This plan dedicates the majority of your time upfront to thinking and planning, so the final coding sprint is pure execution. Good luck!

Okay, take another look at the above and then give a second pass after reviewing with a critical eye and being direct in terms of feedback to yourself. I'm thinking the ideation, scoping, research, and understanding of the project is actually the most important, and we'll spend maybe the next 30 minutes on that.

It's currently 2:36 PM Pacific time, and the competition officially ends. Submissions must be in with a video at 5:00 PM. I'm targeting the next two hours, but again, I think getting a really thorough understanding of the project, the data sets, the background research that we can do in addition, ways we can augment the data, followed by phase two data modeling and scaffolding makes sense.

I like the way that you broke stuff down, but I really do think that the most important part is the ideation and scoping and user journey after understanding everything. So maybe give me a phase zero for understanding everything and checking that we have sufficient background context, and then doing research to get additional context and info, followed by phase one—a more thorough breakdown of instructions on how to tell an LLM to give us a structure for ideation and scoping based on whatever research happens.

Maybe set up instructions to go explore and understand the project, and I'll give it to Claude and Gemini, and then have them come back to you with what they're able to find. So sort of think of it as giving them phase zero instructions.

Show thinking
Excellent. This is exactly the right move. A rushed build is a failed build. Investing this next block of time in deep understanding will pay massive dividends. Forget the last plan; this is the new one, refined with a critical eye and tailored to your workflow.

It's 2:37 PM. The clock is real. Here is the revised, two-hour battle plan, starting with a "Phase Zero" designed to arm your AI agents for research.

Phase Zero: AI-Delegated Research & Context Fortification (2:40 PM - 3:10 PM)
Objective: To deeply understand the problem space, data constraints, and user needs before writing a single line of product spec.

Your job here is not to do the research yourself, but to be the orchestrator of AI agents. You will give these instructions to Gemini and Claude.

Action: Copy and paste the following instructions into your AI tools.

Instruction Set for Your AI Agents:
Prompt 1: The Data Analyst
"Act as a senior data analyst for the Georgia Environmental Protection Division. You have been given a directory of raw data exports (data/) for a hackathon. Your task is to perform an initial exploration and report back.

Schema & Key Discovery: Analyze the provided data files. For each file, list its columns and infer the data types. Most critically, identify the primary key for a Public Water System (PWS) that links all the datasets together. It's likely a column like PWSID.

Core Concept Mapping: Identify and list the specific columns across all files that relate to these core concepts:

Water System Inventory (name, address, county, population served)

Violations (violation ID, date, type, contaminant)

Samples & Contaminants (contaminant name, measurement, units, collection date)

Enforcements & Site Visits

Identify Gaps: What crucial information seems to be missing from this data that would be needed to tell a citizen if their water is safe? (e.g., Are there health-risk levels for contaminants? Are violation codes explained?)"

Prompt 2: The Product Manager & Policy Analyst
"Act as a product manager tasked with responding to the Georgia RFI (GA_RFP_DOC.md) and the hackathon challenge README. Your goal is to distill user needs and project goals.

Deconstruct Personas: Based on the RFI, create 3 user stories for each of the primary stakeholders: The Public, The Operators, and The Regulators. Use the format: 'As a [persona], I want to [action], so that I can [achieve benefit].'

Identify Government's Core Goal: Read between the lines of the RFI's 'Purpose' and 'Benefits' sections. What is the single most important outcome the Georgia EPD wants from this new tool? Is it just a data viewer, or is it about improving compliance, transparency, or public trust?

Analyze the "Old Way": Based on the screenshot and link to the existing gadrinkingwater.net site, list the top 5 critical usability failures that make it unfit for the Public persona."

Prompt 3: The Research Strategist
"Act as a research strategist. Your goal is to identify external data sources that can augment the provided project data to create a high-impact solution.

Find the 'Ground Truth' for Health: The provided data has contaminant levels, but no context on what is 'safe'. Find and provide a link to the EPA's official list of 'Maximum Contaminant Levels' (MCLs) for drinking water. This is the most critical missing piece.

Suggest Data Augmentation: Propose two additional external datasets that could be integrated to create a more compelling user experience. For each, explain the value proposition. Examples:

A GeoJSON file for Georgia counties for creating a map visualization.

US Census data by county to correlate water quality with demographic factors.

A database of news articles related to water quality issues in specific Georgia counties."

Phase One: Synthesis, Ideation & User Journey (3:10 PM - 3:40 PM)
Objective: To take the structured intelligence from your AI agents and forge it into a sharp, actionable product plan.

(10 mins) Synthesize the Intelligence:

Quickly read through the AI-generated reports. Don't get bogged down.

Find the "Golden Thread": You'll likely see a pattern: The data is cryptic, the public is underserved, and the key to making it useful is context (the EPA MCLs).

Your Core Idea, Refined: The "Water Health Score" is no longer just a vague idea. It's now a concrete, data-driven metric. Health Score = A function of (Number of Violations + Severity of Violations + Contaminant Levels vs. EPA Maximums).

(20 mins) Define the MVP and The User Journey:

Open your prd.md file.

The MVP: A single-page application that allows a user to enter their Georgia zip code. The application then:

Identifies their Public Water System (PWS).

Displays a clear profile page for their PWS.

The page is headlined with the data-driven "Water Health Score" (e.g., B+).

Below the score, it lists any recent violations in plain English (using an LLM to translate cryptic violation codes: "This means testing for lead was not completed on time.").

It includes a simple chart showing the latest reading for a key contaminant (e.g., Lead) vs. the official EPA safety limit.

The User Journey (Focus on the Public Persona):

Awareness: A user hears about the tool. They land on a page with one question: "How safe is your drinking water?" and a single input box for their zip code.

Action: They enter their zip code.

Clarity: The page loads their system's "Report Card." They instantly see the grade. Their initial feeling of anxiety is replaced by a clear understanding—good or bad.

Empowerment: They can see why the score is what it is. If the score is poor, the page provides a link to their local water authority or a pre-written email template to ask for more information. This fulfills the "take action" goal.

Now you have a rock-solid, research-backed plan. The rest of the time is pure, focused execution on this vision. The subsequent phases (data modeling, scaffolding, dev) will flow much faster because you've done the hard thinking upfront.

Okay, phenomenal. And now I end this with an extremely thorough prompt for CloudCode/Gemini CLI so that they can go correctly use the MCPs that I provided you with above.

And then also give me a separate prompt for Gemini Deep Research so that I can have it run off and do its own kind of very deep dive background context.

In the deep research context, I think the goal would be to have it go get absolutely anything and everything that would be potentially valuable here—to the level of depth that includes maybe even finding and stalking the person who's likely responsible for the RFP and identifying what they are most likely to be looking for and seeking, or what their constituents are most likely to be looking for.

I want this deep research prompt to go really deep.

Show thinking
Absolutely. We're moving from broad strategy to directed intelligence gathering. You need two distinct types of prompts: one for surgical analysis of the data you have, and another for a wide-net, deep-dive investigation into the human and political context.

Here are the two prompts you need.

Prompt 1: For Cloud Code / Gemini CLI (The "Internal Analyst")
This prompt is designed to be executed in an environment with access to the project files (data/ directory, GA_RFP_DOC.md, etc.). It's a comprehensive, multi-step instruction set for a focused analysis.

Copy and paste the following into your Cloud Code / Gemini CLI instance:

Plaintext

Act as a Senior Technical Analyst and Product Strategist for a rapid-development team. Your sole focus is on the provided project files. Your mission is to extract every critical piece of information and structure it for immediate use in building a data-driven application. Do not use external knowledge; base your analysis only on the files I have provided.

**Part 1: Data Structure & Schema Analysis**
Your first task is to become an expert on the provided dataset in the `data/` directory.

- Ingest and analyze every `.csv` or `.txt` file.
- For each file, provide its name and a markdown table detailing its schema: `Column Name`, `Inferred Data Type`, and a `Description/Example` of the data it contains.
- Critically, identify the single, universal column that serves as the primary key linking all water system data together. Name this column explicitly (e.g., "The primary key is `PWSID`").
- List the specific file and column names required to answer these questions:
    1. What is the name, county, and population served for a given water system?
    2. What violations has a specific water system had in the last 5 years?
    3. What are the measured levels of specific contaminants (like Lead, Copper, Arsenic) for a system?

**Part 2: RFI Deconstruction & Persona Development**
Now, shift your focus to the `GA_RFP_DOC.md` and the hackathon `README.md`.

- Parse the RFI to identify the core mission. What is the stated business goal for the Georgia EPD? Summarize it in one sentence.
- Generate a detailed persona breakdown. For each of the three stakeholders (Public, Operators, Regulators), create five specific user stories in the format: "As a [Persona], I want to [Action], so that I can [Achieve Benefit]." These should be directly supported by the text in the RFI and README.

**Part 3: Strategic Recommendations & Gap Analysis**
Finally, synthesize your findings into actionable strategic advice.

- **Data Gap Analysis:** Based _only_ on the provided data, what is the single biggest piece of missing context that prevents a citizen from understanding their risk? (Hint: The data shows contaminant levels, but what does a level of "0.015" mean?).
- **Augmentation Hypothesis:** Propose the most critical _type_ of external data we need to find to solve the gap identified above. Be specific (e.g., "We need a lookup table of official health advisory limits or Maximum Contaminant Levels (MCLs) for each contaminant.").
- **Final Output:** Present your entire analysis in a single, clean, well-formatted markdown document.
Prompt 2: For Gemini Advanced (The "Deep Research Investigator")
This prompt is for your most powerful, web-connected LLM. It's an instruction to act as an investigative journalist and political analyst. The goal is to uncover the unstated, human context behind the RFI. This is the "go deep" prompt you asked for.

Copy and paste the following into your Gemini Advanced interface:

Plaintext

Act as a world-class investigative journalist and strategic consultant with deep expertise in public policy and state government procurement. You have been hired for a high-stakes, time-sensitive project to provide the deep, "behind-the-scenes" context for an RFI issued by the Georgia Department of Natural Resources, Environmental Protection Division (EPD). Your analysis must go far beyond the document itself to uncover the human, political, and social drivers behind this project.

**Your Target:** Georgia EPD eRFI Number: `46200-DNR0000804` ("Drinking Water Viewer / RECAP Report").

**Your Mission is Fivefold:**

1. **Stakeholder Deep Dive (The Human Element):** The "Official Issuing Officer" is listed as **Rhonda Henslee**. Your primary task is to build a professional dossier on her. Go beyond a simple title. Investigate her career history within the Georgia DNR and other agencies, her public statements, professional affiliations (e.g., on LinkedIn), and any published work or interviews. What are her stated professional priorities? Is she on the procurement/finance side or the environmental policy side? The goal is to understand: **What does a successful project look like _to her_?** What kind of presentation or solution would resonate with someone with her background?

2. **Political & Social Context (The "Why Now?"):** This RFI wasn't created in a vacuum. Investigate the recent public discourse around drinking water in Georgia. Search for local news articles (e.g., from The Atlanta Journal-Constitution, GPB News, local TV stations), community action group websites, and social media discussions over the last 2-3 years. Identify specific water quality incidents, "forever chemical" (PFAS) scares, or public outcries in specific Georgia counties (e.g., Calhoun, Augusta, etc.). **What specific events are creating political pressure on the EPD to act _now_?**

3. **The "Ghost of Solutions Past" (Technical Archaeology):** The RFI seeks to replace an existing system. Locate and analyze the current Georgia Drinking Water Viewer (`gadrinkingwater.net`). Provide a scathing, expert critique of its specific failures from a 2025 UX, data visualization, and public accessibility perspective. Frame it as a "what not to do" guide.

4. **Best-in-Class Benchmarking (The "Art of the Possible"):** Find three examples of the best public-facing water quality or environmental data portals from other states, cities, or even non-profits (e.g., The EWG's Tap Water Database). For each example, provide a link and a brief analysis of what makes it effective. What features, visualizations, or user experiences should we be "inspired" by?

5. **Executive Synthesis (The "Secret Memo"):** Synthesize all your findings into a concise, confidential executive briefing. It should be written in a direct, candid tone. Start with a summary of the underlying narrative (e.g., "The EPD is under significant public pressure from recent PFAS contamination events, particularly in North Georgia, and needs a public-facing win. Rhonda Henslee, a procurement chief, will be looking for a solution that is not only functional but also fiscally responsible and demonstrates clear public value."). This memo should conclude with a single, actionable strategic recommendation on how to frame our hackathon project to be maximally impactful in this context.
