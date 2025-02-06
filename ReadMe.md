# Search Analysis Project

## Business Problem
Users are searching for products on the website, but some searches do not return relevant results, 
have low engagement (CTR), or fail to convert into purchases. This indicates potential issues with search accuracy, 
speed, ranking, and user experience, leading to revenue loss. 

The primary objective is to boost conversion rates to maximize revenue from search traffic. Improve search relevance and
ranking to increase CTR.

## Teams Involved
E-Commerce/Product Team, Engineering (Search Team)

## Key Performance Indicators, KPIs
1. Search Success Rate: % of searches returning relevant results.
2. Click Thru Rate (CTR): % of users clicking on a search result.
3. Search Response Time: Avg. time taken to return search results.
4. Conversion Rate:	% of searches that led to a purchase.
5. Search Failure Rate:	% of searches returning no results.
6. CTR by Search Source: Click rate for Homepage, Category, and Product Pages

## Target Goals for each metric
| KPI                   | Goal   |
|-----------------------|--------|
| Search Success Rate   | >90%   |
| Click Thru Rate (CTR) | >75%   |
| Search Response Time  | < 2sec |
| Conversion Rate %     | > 20%  |
| Search Failure Rate   | < 10%  |
| CTR by Search Source  | Category > Homepage|


## Key Points for Analysis
1. How often do searches fail? 
2. Which search terms have the highest/lowest CTR? 
3. Does search response time affect user engagement? 
4. How do devices impact search behavior? 
5. Which search sources perform best? 
6. What % of Users drop-offs from searching to purchase? 

## Action Plan
1. There is 28.82% of the times the users are not returned any results for their search. 
Dresses, Shoes, Socks and water bottle are the terms which are resulting in no results.

Maybe those products are not in stock or incorrect product categorization or missing products
or the search system may fail to retrieve it due to technical reasons.

![image alt](https://github.com/Bhaktispace/SearchTermAnalysis/blob/dd77e9a8d4aea32535cd264703c56f220c69d763/Images/Q1.PNG)

2. Highest CTR is for gaming chair at 73.6% and the lowest CTR is for Smartphones at 66.6%.
The highest CTR is below the goal of 75%. To improve the CTR consider following: A/B test images 
and title, show discount badges and limited stock alerts, Use email/SMS retargeting users based
on search behavior.

4. Moderate search time has the highest CTR (51.6%), meaning searches that take a moderate amount of time 
lead to more clicks. Very slow query time (48.8%) has the lowest CTR, suggesting that long processing times
reduce engagement. Very slow query times has the highest conversion rate (10.6%), meaning when queries take 
longer, the search results may be more refined, leading to better purchase decisions. Moderate query times
have the lowest conversion rate (8.9%), suggesting that although users engage more (high CTR), 
they may not find exactly what they need. 
Maintain optimized indexing to balance query speed & result quality, Improve query performance with better 
caching, indexing, or query optimization and Ensure high-quality, relevant search results even for 
slow queries.

5. Desktop (71.99%) has the highest success rate, followed by Tablet (71.31%) and Mobile (70.24%). 
Mobile has the lowest success rate, possibly due to smaller screens, less intuitive navigation, or 
slower page loads. Desktop (51.45%) has the highest CTR, indicating that desktop users engage more with 
search results. Mobile has the lowest CTR (48.71%), suggesting that users either abandon searches more often
or struggle to find relevant results. Search time is nearly the same across devices (1.86–1.88s). Since 
search times are similar, the differences in CTR and Success Rate are likely influenced by factors like 
screen size, ease of interaction, or search intent rather than time spent searching. 
Since Mobile has the lowest success Rate and CTR investigate the Mobile UI/UX. Desktop users 
click more and succeed more, maybe we should optimize desktop search experience for deeper enagagement 
like product recommendations.

6. Product Page (71.57%) has the highest success rate, meaning searches from product pages return relevant 
results most often. Homepage (70.91%) has the lowest success rate, indicating that searches from the homepage
may be broader or less targeted. Homepage has the highest CTR (50.66%), suggesting that users searching from
the homepage are more likely to click on a result. Product Page has the lowest CTR (50.06%), indicating that
users searching from product pages might already be browsing and click less. Homepage has the highest 
conversion rate (10.34%), meaning users searching from the homepage are more likely to complete a purchase. 
Product Page has the lowest conversion rate (9.59%), which is surprising given that product pages usually 
indicate higher purchase intent.
Homepage Search Optimization: High CTR and High Conversion rate indicates that users searching from the 
home page are engaged and convert well. Maybe we should consider improving the search relevance further to 
increase success rates.
Product PAge: Improve conversion Funnel, users search often but convert less suggesting they might not 
find what they need. The potential reasons can be to improve product page recommendations.

7. There is a drop-off after clicking on the search results. The possible reasons could be:
Pricing Issue, Lack of reviews, unclear product details or Checkout friction.
