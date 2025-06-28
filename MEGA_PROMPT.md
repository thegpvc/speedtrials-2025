# Megaprompt

Hey, okay, so I'm currently at this hackathon in San Francisco. Basically what's going on is it's a speed trials or speed coding challenge in which one person per team (or one human per team) is allowed, and you're meant to take advantage of AI coding tools and similar in order to actually get shit done as fast as possible. That's really the idea.

What I am going to do is I'm looking for your help breaking down the remaining, let's say two, two and a half hours into the optimal way to use the time. I imagine it's going to look like a structure similar to using the first X amount of time as research, then scaffolding out what we actually want to do, imagining the user experience, making sure that we thoroughly understand the problem. I think a lot of this is going to be data model and problem space.

So I'm going to switch microphones here. I basically want you to help me do the initial thinking and scaffolding out, plan out the research that we'll need to do. I'm looking to do something where I'm not really too concerned about winning this thing, but it's more along the lines of doing stuff in an interesting way, I think. Taking advantage of some of the newer tools, like Worktrees approaches, Gemini CLI, etc. That's more what I care about.

But help me kick this thing off. 


—


...


—

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



**Event Name:  Drinking Water Viewer / RECAP Report**



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

2. Second, the State Entity may also provide documents in the section of the Event entitled “eRFI Questions”.  To the right of each question appearing under the eRFI Questions section, the Event contains an icon (appears as a bubble with text).  By selecting this icon, the supplier will navigate to a new page of the Event.  On this new page the supplier can locate attached documents.



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



In the early 1990s, EPA set out to provide important drinking water agencies with an information system that would not only report accurate data to the federal system on a timely basis but would also support the rule implementation activities of primacy agencies so that these agencies would not have to develop an information system on their own.  That system, known as the Safe Drinking Water Information System (SDWIS/STATE), needed to be efficient enough to enable compliance determination for a host of growing EPA regulations, and it needed to gain acceptance by addressing the specific needs of a large and varied base of primacy organizations.



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



https://gadrinkingwater.net/DWWPUB/







### Bid Banana - Drinking Water Viewer / RECAP Report



https://bidbanana.thebidlab.com/bid/V3T5BeqhF6PnZhyeAJyr



### GA gov site - already downloaded and converted to markdown as GA_RFP_DOC.md



https://fscm.teamworks.georgia.gov/psp/supp/SUPPLIER/ERP/c/DX_SRM_MENU.DX_AUC_EVENT_ATTCH.GBL?PORTALPARAM_PTCNAV=DX_AUC_EVENT_ATTCH_GBL&EOPP.SCNode=ERP&EOPP.SCPortal=SUPPLIER&EOPP.SCName=EPAUC_PREPARE_BID&EOPP.SCLabel=Manage%20Events%20and%20Place%20Bids&EOPP.SCPTfname=EPAUC_PREPARE_BID&FolderPath=PORTAL_ROOT_OBJECT.EPAUC_PREPARE_BID.DX_AUC_EVENT_ATTCH_GBL&IsFolder=false&SearchAction=DirectLink&BUSINESS_UNIT=46200&AUC_ID=DNR0000804



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

