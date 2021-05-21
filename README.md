# Formula 1 Pitstop Strategy

<!-- wp:paragraph -->
<p>A Big Data Analytics project initiative on Formula One racing.</p>
<!-- /wp:paragraph -->

<!-- wp:spacer {"height":45} -->
<div style="height:45px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->

<!-- wp:group -->
<div class="wp-block-group"><div class="wp-block-group__inner-container"><!-- wp:image {"align":"left","id":2852,"width":178,"height":178,"sizeSlug":"large","className":"is-style-rounded"} -->
<div class="wp-block-image is-style-rounded"><figure class="alignleft size-large is-resized"><img src="https://wp.cs.hku.hk/wp-content/uploads/Ross-Brawn-1.jpg" alt="" class="wp-image-2852" width="300" height="300"/></figure></div>
<!-- /wp:image -->

<!-- wp:pullquote -->
<figure class="wp-block-pullquote"><blockquote><p>"It was an innovative approach of an existing idea, and Formula One is all about innovative design. It's a cornerstone and objective of the sport." — Ross Brawn</p></blockquote></figure>
<!-- /wp:pullquote -->

<!-- wp:spacer {"height":45} -->
<div style="height:45px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer --></div></div>
<!-- /wp:group -->

<!-- wp:cover {"url":"https://wp.cs.hku.hk/wp-content/uploads/Pitstop-2.jpg","id":2827} -->
<div class="wp-block-cover has-background-dim"><img class="wp-block-cover__image-background wp-image-2827" alt="" src="https://wp.cs.hku.hk/wp-content/uploads/Pitstop-2.jpg" data-object-fit="cover"/><div class="wp-block-cover__inner-container"><!-- wp:paragraph {"align":"center","placeholder":"Write title…","style":{"typography":{"fontSize":31}}} -->
<p class="has-text-align-center" style="font-size:31px">Scuderia Ferrari Pit-stop for Charles Leclerc, Spanish GP 2020</p>
<!-- /wp:paragraph --></div></div>
<!-- /wp:cover -->

<!-- wp:nextpage -->
<!--nextpage-->
<!-- /wp:nextpage -->

<!-- wp:spacer {"height":22} -->
<div style="height:22px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->

<!-- wp:heading {"level":1} -->
<h1>Project Background</h1>
<!-- /wp:heading -->

<!-- wp:heading -->
<h2>Formula One: The king of motorsport</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Formula One has been the top motorsport racing event worldwide for 70 years. While the constructors compete by developing their engine and chassis with the latest technologies, real-time race simulations are also conducted back in the factories to provide useful insights that could greatly affect team decision making before and during the race. The results are sent to the pit wall, where the race engineers make pit stop strategy decisions and communicate with the drivers and all pit crew members.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Recently in 2019, the FIA (F1 official) has generously made racing data available, a move that immensely lower the barrier to data mining and analytics from the public. Supported by motorsportstats.com, the online database gives numeric details of every historical race, such as lap time, pit stop decisions, driver and constructor championship scores, circuit and weather data, etc. Along with trust-worthy third-party data providers online such as STATS F1, Ergast, Kaggle, and more, we could gather sufficient pieces of data that formulate a digital version of every F1 race.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In this multi-million-dollar industry, a digital war has never been fiercer among back-end factories of each constructor team. Although it is widely known that every competitor possesses such facilities that serve as strategy suggestions, most of the details of how the simulation machines and algorithms are hidden from publicity for two apparent reasons: fear of being copied by competitors, and the enormous amount of resources put into the research and development.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>In light of increasing audience engagement, F1 engaged with the AWS team to provide real-time analytical summaries graphically to let the audience gain effectively more insights about the race. Examples of insights include chasing distance between two competitors, predicted pit-stop strategy, and the probability of overtaking. This opens a new door to transform how audiences traditionally watch a car race, by feeling how close a car chase is even if the two cars are a pit stop apart (at approximately 30 seconds apart from each other). Increasing effort in new features and improvement in prediction accuracy has been seen in the 2019 and 2020 seasons as AWS takes bold strides on committing consistent developments.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Motivation of the project</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In the past decade, top teams such as Mercedes Benz, Scuderia Ferrari, Red Bull, and McLaren F1 Racing has committed huge and fatal pit-stop strategy calls, costing them victories or even the championships. Infamous instances include the 2012 Abu Dhabi GP Alonso’s too-early pit-stop, 2015 Monaco GP Hamilton too-late pit-stop, and the list goes on. When car competitiveness and driver skill level have marginal distinctness, the pit-stop strategy can be very decisive, if not determinant, to the race result. A good pit-stop allows overtaking without even a high-risk close car fight, while a bad pit-stop could put the car in traffic, harming the tyres and the possibility to make overtaking maneuvers.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The major motivation of this project stems from the persistently unsatisfactory performance in the racing strategy of the Scuderia Ferrari F1 Team throughout recent seasons. While the analytical prediction of tyre degradation, gas consumption, and checking of car condition perform up to standard, Ferrari passively reacts to racing incidents and make slow pit-stop decisions after observing how the other teams react. This project serves as a plug-and-use for Scuderia Ferrari as a useful reference to make pit-stop calls by considering all race factors. The project should also standalone be a general prediction model of race result if it is fed with real-time racing data during a race</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1} -->
<h1>Project Objective</h1>
<!-- /wp:heading -->

<!-- wp:heading -->
<h2>Main Objective</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In this project, the main objective is to build a system that is trained with historical race data to predict the optimal pit-stop strategy for the two drivers in the Scuderia Ferrari F1 Team. The system should consider a wide range of factors that are collected in real-time, so as to dynamically generate a prediction about the position when the race evolves, hence optimizing the race results of the 2 Ferrari drivers by selecting the best pit-stop strategy with the least time spent on any human decision-making processes.</p>
<p>Since we have to evaluate the accuracy of our model, our next goal is to use recent F1 seasons as testing data and reach an accuracy rate of >= 70% of predicting final track position after adopting a certain pit-stop strategy.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1} -->
<h1>Project Methodology</h1>
<!-- /wp:heading -->

<!-- wp:heading -->
<h2>Data Source and Data Collection</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>This project relies on several main data sources, including FIA F1 official website, STATS F1, Ergast, McLarenf-1, and also Kaggle for open-source data sources. F1 TV subscription provides telemetry data and traditional live broadcast services for live real-time data analytics. General relational database management software will be adopted for data storage after conducting data cleansing.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Machine Learning</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>This project adopts machine learning for precise predictions and constant refinement of the prediction model. Feeding the learning model with previous race data, it should create a balanced equilibrium of all factors influencing pit-stop strategy. AWS SageMaker is planned to facilitate this task, and Amazon S3 will also be employed for storage purposes. We will use the most recent seasons for the initial stage since they have the closest relevancy to the regulations of the current season, such as regulations on car design, fuel usage, track design, etc. The project will then extend to older seasons as well as including qualifying results and free practice results for evaluation of car performances during the final phase.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Data Visualization and Decision Support System (DSS)</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Decision Support System is the interface for race engineers to evaluate and deploy the analysis results. We planned to subscribe to a third party DSS provider for their design layout, but we are still in search of which platform to use. Graph visualization could also be conducted through the use of D3.js for a better understanding of data analysis results. The user interface must be real-time, highly interactive, as clear and simple as possible.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1} -->
<h1>Experiments and Results</h1>
<!-- /wp:heading -->

<!-- wp:heading -->
<h2>Machine Learning Model 1: Predict final position gain or loss</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We adopted Tensorflow Keras Sequential model for predicting position gained or lost at the end of the race when given a set of factors as input. This is a supervised regression type machine learning model where we feed the model with 17 input factors and 1 result label about the gain or loss in the final position.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h3>Final Model design architecture</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>For dividing the training data set and testing data set, we decided to split the data set by pandas.sample function to divide 20% of validation data randomly from the entire data source for each epoch during the training process. Afterwards, we used preprocessing.Normalization function from Tensorflow Keras Regularizers module to normalize all feature labels. At each of the 10 layers of the model, we implemented ReLU activation function because ReLU has a linear behavior which makes optimization easier for the neural network. L2 regularizers were also implemented at the rate of 0.001 for each Dense layer, with a Dropout layer at the rate of 0.5 in between each layer. Mean squared error (MSE) was used for the loss function since it is insensitive to outliers and errors, and RMSprop for optimizer since it is a very robust optimizer and ideal for deepnets. There were 1135 records from 2016-2020 season, and 934 records from 2016-2019 season.</p>
<p>In the 2020 season, the total average accuracy index is 2.227799, which in other words the final position prediction would have ±2.227799 error.
An important fact about predicting the 2020 season is that Formula One has introduced a brand new “Corona calendar” with 5 new tracks that nobody has ever raced before. It demonstrates that how our generalization of tracks by their respective characteristics effectively helps to predict not only traditional race circuits, but even new racetracks as well. This is an important indication of how accurate, reliable, and useful this model is to the Scuderia Ferrari Team for extensive future use.
</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Machine Learning Model 2: Predict pitstop strategy under Safety Car condition</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Similar to Model 1, we adopted Tensorflow Keras Sequential model for predicting the final position gain or loss under two scenarios: the racer goes in for a pitstop when the safety car is deployed; Or the racer stays out on the track, together with some race facts at the moment when the safety car is deployed. This is a supervised regression type machine learning model where we feed the model with 15 input factors and 1 result label about the gain or loss in the final position. Before proceeding to the model design evolution, more explanation and discussion of the “safety car scenario” would be provided first.
</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h3>Pitstop strategy difference under Accident Scenario</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Formula One is never a peaceful sport. Especially since the race adopted a standing start, where all cars start from a standing grid and accelerate at the same time, there are always side-to-side battles and car crashing during the opening lap, or even the first corner of the track (a.k.a. first lap drama). Whenever there is a hazard caused by accidents on the track, such as a sudden engine failure of a car, car crashing to a wall or with other cars, a yellow flag will be raised, and either a safety car will be deployed to lead the race in a relatively slower pace, or a Virtual Safety Car (VSC) will be deployed where all drivers are forced to drive slowly by maintaining a delta, which is a speed restrictor that limits racing pace. In either of the situations, all cars are required to drive at a slower speed to let the marshal (staff members of the track) clear off the debris and all other blockages on the track.</p>
<p>Under such a scenario, a lot of drivers would decide to alter their original planned pitstop strategy and pit in earlier than planned. The reason is that during a normal racing lap, the time spent on going into the pit stop and change tyres could be around 30 seconds, and after the pit stop, the driver would be demoted to a position 30 seconds behind his current position, which would always be an immense drop in positions since the time difference between each driver is very small, accounting for few milliseconds difference per lap; However, under the Accident scenario where the safety car or VSC is deployed, all cars running on the track must slow down, such that after going into a pit stop, the driver will not be demoted 30 seconds behind, but most likely halved or even less, because the rivals who are originally 30 seconds behind the driver must drive slowly and therefore cannot catch up the driver going into the pit stop, making that 30 seconds cost virtually less time-consuming.</p>
<p>However, it remains controversial whether the driver should change its planned pitstop strategy and get a “free pit-stop”, because there is still position loss to suffer from going into a pitstop. Some circuits are harder to make overtaking maneuvers and therefore holding position is more important than having fresher tyres for higher car performance. It creates a dilemma for the team and the drivers whether they should sacrifice track position for fresher tyres and better grip, hence better car performance, or stay out at the track to possibly gain some positions due to others choosing to go into the pitstop. The model is therefore aimed to evaluate the benefits of making a pitstop under such an Accident Scenario quickly as to let the team reacts as soon as the safety car is deployed, hence maximize the pit crew members’ time for preparing the tyres and get ready in position.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h3>Dataset Description</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The list of input factors are as follows:
<ol>
  <li>Initial starting position of the racer.</li>
  <li>Lap number when the safety car is deployed.</li>
  <li>Laps travelled for the current tyre set.</li>
  <li>Laps remained of the race.</li>
  <li>Current tyre compound.</li>
  <li>Current position</li>
  <li>Track temperature.</li>
  <li>Track humidity.</li>
  <li>Track maximum altitude change.</li>
  <li>Track number of turns in a lap.</li>
  <li>Track race distance / total number of laps.</li>
  <li>Track total length of race (in km).</li>
  <li>Team Ability index (from previous season constructors’ championship points).</li>
  <li>Driver Ability index (from previous season drivers’ championship points).</li>
  <li>Binary decision of whether the car goes in for a pitstop.</li>
</ol>
</p>
<p>Our training label (result) is also the final position gain or loss, which reflects on how good different strategies are. By varying the input column of “binary decision of whether the car goes in for a pitstop”, we compare the two predicted final position gain as to understand which decision would benefit the racer the most, whether to go into the pitstop or not when the safety car is deployed.</p>
<p>The result shows that the first model that was trained with 2016-2018 seasons have ±2.4674 final position difference in 2020 season, which is higher than ±2.0999 of the last model trained with 2016-2019 season. There is also an observable decreasing trend of the accuracy index from the first to the last model. We may conclude that including more seasons in the future would improve the accuracy of the model.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Decision Support System</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>To demonstrate how the race strategist in the Scuderia Ferrari F1 Team could use the model to swiftly come up with a pitstop strategy decision, we make a simplified DSS that provides a real-time prediction function by accessing the two established models, which are predicting final position gain or loss, and predicting pitstop strategy under Safety Car conditions, respectively.</p>
<p>We provide a simple Python program with a command line interface, with guidance that leads the user to input the predicting team, racer, and the corresponding required race information. The user is only required to use the numeric keypad to navigate through the DSS, such that the least amount of typing is required to arrive at the wanted predictions.
</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":1} -->
<h1>Conclusion and Future Works</h1>
<!-- /wp:heading -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We have established our first model that predicts position change when given a pitstop strategy and track condition, under dry conditions. The first model gives us huge confidence that Scuderia Ferrari F1 Team could start relying on the prediction results and make more optimized pit stop strategies in future seasons. When testified by the 2020 season races, the model predicts the final position with ±2.2278 absolute position difference on average.</p>
<p>Our second model helps strategists make a quick decision during an Accident scenario with the safety car deployed. The team can swiftly react to the sudden potential pitstop decision by running the model for the predicted final position gain, in order to realize if the decision to pit in or stay out could give them the optimized race result. When testified by the 2020 season races, the model predicts the final position with ±2.0999 absolute position difference on average. This testing method would serve as the best examination method, since we cannot alter historical decisions and check the real-life result of “what if he did not pit in or did not stay out”. However, we proved that by including more future race results in the model, the accuracy of the final position prediction would increase.</p>
<p>Our simplified Decision Support System functions fundamentally as we wished. By quickly gathering the required information from the user, the program promptly arrived at the pitstop strategy suggestions and their corresponding final position predictions. It could therefore effectively save time for the race strategists to form a final race strategy decision.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Improvement</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>However, the models still have areas to be improved. Firstly, without knowing the opponent’s pitstop strategy decisions, the first model could only predict outcomes for a specific predefined scenario from racing strategists. In addition, wet weather conditions could imply different tyre strategies, which is not covered in our model training process. Regarding the optimal number of pitstops, from the 2016 season onwards, 1-stop and 2-stop pitstop decision predominates the races, and 3-stop strategies or more stops tend to give worse results. However, 3-stop might still be the optimal strategy especially under several safety car scenarios. Both of our models disregard successful or unsuccessful 3-stop pitstop strategies.</p>
<p>These mentioned scenarios are not taken into full consideration in the training process, hence unable to deliver predictions during wet conditions and more than 2-stop pitstop strategies, limiting the use cases of the system. More discussion on how to improve the model’s accuracy would also be provided in the “future work” section below.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Future Works</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Our future works include the followings:</p>
<b>Current Model improvement:</b>
<ol>
  <li>Improve Driver & Team Ability index score.</li>
  <li>Confidence score for prediction results.</li>
</ol>
<b>Model functionality extension:</b>
<ol>
  <li>Model for predicting opponent’s pitstop strategies.</li>
  <li>Model that predicts position gain or loss under wet conditions and DNF.</li>
  <li>Data visualization & Dynamic Decision Support System (DSS).</li>
</ol>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h3>Improve Driver & Team Ability index score</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Currently, the model attempts to give credits to better constructor teams and drivers by an index score, so to differentiate competitive cars and racers from the weaker cars and inexperienced drivers. An intuitive way is to take the constructor championship scores and driver championship scores from the previous year. However, a driver’s ability should be related to the experience the driver has and his driving style, and the fact that the driver’s score from last season might be greatly affected by the car’s competitiveness creates inaccuracy to the index score. An example would be Scuderia Ferrari F1 Team driver Charles Leclerc, who drove for Sauber Ferrari F1 Team (former of Alfa Romeo Racing), which has not been a competitive constructor team over recent years. To improve the driver ability index score, it is possible to take a driver’s previous races in other championships, such as Formula 2 or Formula 3, as a reference to how the driver performs.
<p>Throughout the years, constructor teams’ competitiveness has also varied a lot. For Scuderia Ferrari F1 Team, it finished sixth place in the constructor championship in 2020, which is the worst season in 40 years: Even for the performance in 1980, it was a “sudden, brief dip” in the team’s form, and were the championship the year before, and were back on top within two seasons (RaceFans, 2020). Our model suffers from prediction accuracy as a result of the sudden drop in Ferrari’s car performance, hence we have to update the teams’ ability index with the 2020 season constructor championship score instead. To solve this problem, we could take reference of the race pace of teams during each race qualifying session, where all cars will try to make the fastest lap time in order to start from front positions. In addition, free practice session could serve as a durability test, that could also contribute to the team ability index in the model.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h3>Confidence score for prediction results</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Our model could provide insightful predictions about final positions or pitstop strategy suggestions during the safety car scenario, with a model accuracy of approximately ±2 absolute position difference. However, it lacks a confidence score of how confident the prediction is. An improvement in providing the confidence level could help the well-informed race strategists form a better decision. To facilitate this feature, we may have to change the result label to a categorized result label, for example, a category for each integral final position. Next, we could use Explainable AI to run an analysis on the confidence level of each prediction for each category. The drawback of such an approach is that, when applied to model 2 about accident scenario, we cannot provide predictions on final position gain to 4 decimal points to compare whether staying out or pitting in would be a better strategy option. However, it still remains an immense reference value of how sure the model thinks about the prediction results.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h3>Model for predicting opponents’ pitstop strategies</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Famous Chinese philosopher Sun Tzu once said, “know your enemy and know yourself, you will not be imperiled in a hundred battles.” F1 pitstop strategy will not be complete if we fail to predict the opponents’ strategies. However, due to the zero-sum game nature of Formula One, game theory suggests that different teams would react aggressively to opponents’ racing strategies, including pitstop strategies, attacking or conservative driving, undercutting or overcutting, etc. This problem could not be simply solved by adopting a similar model like our two models, since inclusion of all opponent’s racing strategies is required to understand how different racers interact with state changes and decisions made by opponents. A more sophisticated and advanced Artificial Intelligence model such as a multi-agent reinforcement learning model might be required for predicting how each racer as an individual agent should gain the optimal benefits by conducting what actions at what time.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h3>Model that predicts position gain under wet conditions and DNF</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Our model neglects all historical races under wet or mixed-weather conditions, which occasionally occur in a regular F1 calendar. While dry-weather conditions mainly challenge the car’s performance, durability, and the execution of pitstop strategies, wet-weather conditions testify drivers’ racecraft and skillsets, which include how well the driver handles cornering with much less grip between the tyres and the floor, and whether the driver can correct and save the car when it loses control.
<p>In addition to wet-weather conditions, if a racer crashed the car or retired from the race due to any reason, the label “DNF” which stands for did-not-finish would be applied to the record. Although in our model design we ignore such records and only focus on those with a race end result, the DNF records may stand for some implications, such as an over-aggressive tyre strategy that cause an overly degrading of tyres, that leads to spinning out off the track and crashing the car. However, there are also situations such as engine, suspension, or braking system failures, etc. These situations are uncontrollable regarding how the racing strategies are conducted, hence should not be included in the consideration. A throughout categorization of DNF records is needed to understand the cause of the car retirement, so that we could build a model that tries to avoid falling into the same situation of race retirement.
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h3>Data Visualization and Decision Support System (DSS)</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Decision Support System is the interface for race engineers to evaluate and deploy the analysis results. The system should be simple, providing a set of neat input rows and a clear prediction result to update the team strategists effectively and efficiently. The user interface must be supporting real-time updates, highly interactive with high clarity. By updating the race condition in real-time, the system will simulate all possible pit-stop strategies at every lap dynamically and generate reports on each outcome. After ranking all outcomes, the system should suggest to the user on which lap should the car be pitted in for new tyres, with the probability of the predicted resulting track position.
<p>By making a user interface with predictions and strategy suggestions, we could develop several easily interpretable data visualization tools such as interactive charts showing how different pitstop strategies affect different attributes such as final position, risk factors, or even to show comparisons of different suggested strategies.
From the literature review, we know the fatal mistake made in Abu Dhabi 2010 is due to the over-reliance on the system, and there are only 2 choices made by the DSS. In our design, we should emphasize providing a larger variety of optimal pit stop strategies and let the strategists more freedom to choose from several options.
<!-- /wp:paragraph -->

<!-- wp:image {"align":"center","id":1093,"width":224,"height":288,"sizeSlug":"large","className":"is-style-default"} -->
<div class="wp-block-image is-style-default"><figure class="aligncenter size-large is-resized"><img src="https://wp.cs.hku.hk/wp-content/uploads/profile-photo.jpg" alt="" class="wp-image-1093" width="224" height="288"/></figure></div>
<p class="has-text-align-center" style="font-size:31px">Mentee: Chan M. C., Jack</p>
<!-- /wp:image -->

<!-- wp:image {"align":"center","id":1094,"width":229,"height":278,"sizeSlug":"large"} -->
<div class="wp-block-image"><figure class="aligncenter size-large is-resized"><img src="https://wp.cs.hku.hk/wp-content/uploads/prof.jpg" alt="" class="wp-image-1094" width="229" height="278"/></figure></div>
<p class="has-text-align-center" style="font-size:31px">Supervisor: Professor Choi, Y. K., Loretta</p>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>For enquiries, please contact me at jackchan0528@gmail.com</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Thank you!</p>
<!-- /wp:paragraph -->
