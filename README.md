# WebScraping
<br>
<h3> This repository contains projects related to Web Scraping </h5>
<h4>The first project is based on extracting data for internship listings related to Machine Learning on Internshala</h4>
<br>
<p>
  The project aims to extract useful information such as the Job Role, Company Name, Duration of Internship, among others.

  <ul>Python Libraries Used:
  <li>Beautiful Soup</li>
  <li>Requests</li>
  </ul>
</p>
<br>

### **Extracting data from tags containing similar class type** 

I am facing a problem in obtaining the data for the duration of Internship from the below mentioned tag:

`<div class="item_body"> 3 Months  </div>` tag
because of a tag containing similar class:
`<div class="item_body" id="start-date-first">`
     `<span class="start_immediately_mobile">Starts&nbsp;<immediately</span>`

> Output:
<br>
0.
Company_Name -> AgentInsights
Job_Role -> Computer Vision
Duration ->
Starts immediatelyImmediately

<br>
> Desired Output:
<br>
0.
Company_Name -> AgentInsights
Job_Role -> Computer Vision
Duration -> 3 Months
<br>
Author- Richa Mishra
<br>
`EDIT: Problem has been resolved!`
