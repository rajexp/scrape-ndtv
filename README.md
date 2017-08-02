# scrape-ndtv
Demo script of scraping NDTV website for getting lastest news  
This script returns the latest news from [NDTV](http://www.ndtv.com) website.  
Supported on __Python 3__  
`get_latest()` method returns the list of recent articles in JSON format 
# Demo data
  `[
   {  
    'image': 'https://i.ndtvimg.com/i/2017-06/students-in-exam_240x180_41496727138.jpg', 
    'link': 'http://www.ndtv.com/india-news/cabinet-junks-no-detention-policy-class-5-and-8-students-can-fail-again-1732765', 
    'content': 'The Union Cabinet has approved the scrapping of the no-detention policy in schools till Class 8. An enabling provision will be made in the Right of Children for Free and Compulsory Education Amendment Bill which will allow states to detain students in class 5 and class 8 if they fail in the year-end exam.', 
    'title': 'Cabinet Junks No-Detention Policy, Class 5 And 8 Students Can Fail Again'},
    {
     'image': 'https://i.ndtvimg.com/i/2017-07/vikram-goud_240x180_71501227973.jpg', 
     'link': 'http://www.ndtv.com/hyderabad-news/congress-leader-vikram-goud-wanted-sympathy-to-contest-polls-paid-shooters-50-lakh-cops-1732763', 
     'content': "Vikram Goud, the son of a former Andhra Pradesh minister, was rushed to Hyderabad's Apollo Hospital with multiple bullet injuries last week. But once the police initiated a probe, Vikram, from victim, turned main suspect.", 
     'title': 'Congress Leader Vikram Goud Wanted Sympathy To Contest Polls, Paid Shooters 50 Lakh: Cops'},
     ........ more articles
   ]`  
   
## Fields Description
  1.  __image__   : link of the image in the article  
  2.  __link__    : article's url  
  3.  __content__ : The condensed headstory of the news  
  4.  __title__   : Title of the news article
  
    
