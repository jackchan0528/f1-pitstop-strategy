# f1-pitstop-strategy
 A pit-stop optimization strategy project on Formula One racing

Formula 1 Pit-Stop Strategy
Project Background
Formula One: The king of motorsport
Formula One has been the top motorsport racing event worldwide for 70 years. While the constructors compete by developing their engine and chassis with the latest technologies, real-time race simulations are also conducted back in the factories to provide useful insights that could greatly affect team decision making before and during the race. The results are sent to the pit wall, where the race engineers make pit stop strategy decisions and communicate with the drivers and all pit crew members.

Recently in 2019, the FIA (F1 official) has generously made racing data available, a move that immensely lower the barrier to data mining and analytics from the public. Supported by motorsportstats.com, the online database gives numeric details of every historical race, such as lap time, pit stop decisions, driver and constructor championship scores, circuit and weather data, etc. Along with trust-worthy third-party data providers online such as STATS F1, Ergast, Kaggle, and more, we could gather sufficient pieces of data that formulate a digital version of every F1 race.

In this multi-million-dollar industry, a digital war has never been fiercer among back-end factories of each constructor team. Although it is widely known that every competitor possesses such facilities that serve as strategy suggestions, most of the details of how the simulation machines and algorithms are hidden from publicity for two apparent reasons: fear of being copied by competitors, and the enormous amount of resources put into the research and development.

In light of increasing audience engagement, F1 engaged with the AWS team to provide real-time analytical summaries graphically to let the audience gain effectively more insights about the race. Examples of insights include chasing distance between two competitors, predicted pit-stop strategy, and the probability of overtaking. This opens a new door to transform how audiences traditionally watch a car race, by feeling how close a car chase is even if the two cars are a pit stop apart (at approximately 30 seconds apart from each other). Increasing effort in new features and improvement in prediction accuracy has been seen in the 2019 and 2020 seasons as AWS takes bold strides on committing consistent developments.

Motivation of the project
In the past decade, top teams such as Mercedes Benz, Scuderia Ferrari, Red Bull, and McLaren F1 Racing has committed huge and fatal pit-stop strategy calls, costing them victories or even the championships. Infamous instances include the 2012 Abu Dhabi GP Alonso’s too-early pit-stop, 2015 Monaco GP Hamilton too-late pit-stop, and the list goes on. When car competitiveness and driver skill level have marginal distinctness, the pit-stop strategy can be very decisive, if not determinant, to the race result. A good pit-stop allows overtaking without even a high-risk close car fight, while a bad pit-stop could put the car in traffic, harming the tyres and the possibility to make overtaking maneuvers.

The major motivation of this project stems from the persistently unsatisfactory performance in the racing strategy of the Scuderia Ferrari F1 Team throughout recent seasons. While the analytical prediction of tyre degradation, gas consumption, and checking of car condition perform up to standard, Ferrari passively reacts to racing incidents and make slow pit-stop decisions after observing how the other teams react. This project serves as a plug-and-use for Scuderia Ferrari as a useful reference to make pit-stop calls by considering all race factors. The project should also standalone be a general prediction model of race result if it is fed with real-time racing data during a race

Project Objective
Main Objective
In this project, the main objective is to build a system that is trained with historical race data to predict the optimal pit-stop strategy for the two drivers in the Scuderia Ferrari F1 Team. The system should consider a wide range of factors that are collected in real-time, so to dynamically generate position information and chasing distances before and after possible pit-stop at each lap, hence optimizing the pit-stop strategy by selecting the pit-stop that creates the best result in terms of track position and probability of overtaking.

Stage Goals
To achieve our main objective, we break the project down to several stage goals. For the use of historical race data, we need to find out the correlation between these factors:

Laps undercut VS possibility of undercut
Laps overcut VS possibility of overcut
Change in tyre compound VS gain/loss in track position before the next tyre change
Track temperature VS tyre compounds lifespan
Track altitude change VS tyre compounds lifespan
Undercut and Overcut possibility change under wet and half-wet conditions
Undercut and Overcut possibility change under high and low downforce car set-up
Gentleness of throttle and braking VS tyre lifespan
Number of overtake maneuvers VS tyre lifespan
Driving style and preference of oversteer and understeer VS tyre lifespan
Pit decisions under safety car / virtual safety car conditions
More factors to be explored in later stages.
The next goal is to build a system that can read in real-time data input, such as information about track position, weather condition, overtakes, delta lap time, etc. It will simulate all possible pit-stop strategies at every lap dynamically and generate reports on each outcome. After ranking all outcomes, the system should suggest the user on which lap should the car be pitted in for new tyres, with the probability of the predicted resulting track position.

Since we have to evaluate the accuracy of our model, our next goal is to use recent F1 seasons as testing data and reach an accuracy rate of >= 70% of predicting final track position after adopting a certain pit-stop strategy.

Project Methodology
Data Source and Data Collection
This project relies on several main data sources, including FIA F1 official website, STATS F1, Ergast, McLarenf-1, and also Kaggle for open-source data sources. F1 TV subscription provides telemetry data and traditional live broadcast services for live real-time data analytics. General relational database management software will be adopted for data storage after conducting data cleansing.

Machine Learning
This project adopts machine learning for precise predictions and constant refinement of the prediction model. Feeding the learning model with previous race data, it should create a balanced equilibrium of all factors influencing pit-stop strategy. AWS SageMaker is planned to facilitate this task, and Amazon S3 will also be employed for storage purposes. We will use the most recent seasons for the initial stage since they have the closest relevancy to the regulations of the current season, such as regulations on car design, fuel usage, track design, etc. The project will then extend to older seasons as well as including qualifying results and free practice results for evaluation of car performances during the final phase.

Data Visualization and Decision Support System (DSS)
Decision Support System is the interface for race engineers to evaluate and deploy the analysis results. We planned to subscribe to a third party DSS provider for their design layout, but we are still in search of which platform to use. Graph visualization could also be conducted through the use of D3.js for a better understanding of data analysis results. The user interface must be real-time, highly interactive, as clear and simple as possible.

Project Schedule and Milestones
Date	Milestones
Week 1-3	Set-up of AWS Project, test-run AWS ML API services, scrap all race data from 2019 F1 season
Week 4-5	Use stage goal 1 and 2 (Laps undercut VS possibility of undercut, and Laps overcut VS possibility of overcut) to train the model. Try to predict other historical race events with the model and judge the correctness.
Week 6-7	Refine the model according to test results. Enlarge the scope to include stage goals 3, 4, 5 to the factors, check correctness by using historical race events.
Week 8-10	Refine the model. Enlarge the scope to stage goals 6, 7, 8. Start working on DSS user interface.
Week 11-13	Stage goals 9, 10, 11, and new factors can be introduced. DSS should be fundamentally functional by the end of this stage. Start importing and using 2018, 2017 race data to train the model.
Phrase 1: 4th Oct 2020 – 31st Dec 2020
Date	Milestones
Week 1-3	Buffer period for catching up unfinished goals from Second Phrase. Finish the interim report and prepare for the first presentation.
Week 4-6	2020 season should have ended on 13 Dec 2020. We would replay selected race events and evaluate our current system model. We will devise a simulator of events, sourced from race replay at F1 TV, to mock a real-time race event and adopt our system. Prediction precision should exceed 70% at this stage. Modification of our model according to the evaluation result will be conducted.
Week 7-9	If further modification is not needed, we analyze the race data from qualifying sessions of 2019, including Q1, Q2, and Q3. Categorizing the qualifying data to be used in training the model, and then use it to train the model.
Week 10-12	Start making a 3-minute video and start writing the final report. Apply final adjustments and fixes to the system.
Week 13-15	Start preparing for the final presentation. Finish the 3-minute video and the final report.
Phrase 2: 1st Jan 2021 – 18th Apr 2021

Mentee: Chan M. C., Jack

Supervisor: Professor Choi, Y. K., Loretta
For enquiries, please contact me at jackchan0528@gmail.com, or via phone at +852 98233530

Thank you!

To be updated every Saturday!
