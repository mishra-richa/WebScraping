# WebScraping
<br>
<h5> This repository contains projects related to Web Scraping </h5>
<h4>The first project is based on extracting data for internship listings related to Machine Learning on Internshala</h4>
<br>
<p>
  The project aims to extract useful information such as the Job Role, Company Name, Duration of Internship, among others.

  <ul>Python Libraries Used:
  <li>Beautiful Soup</li>
  <li>Requests</li>
  </ul>
</p>

<title> Extracting data from tags containing similar class type </title>


<p>
I am facing a problem in obtaining the data for the duration of Internship from the below mentioned tag:

&lt;div class="item_body"&gt; 3 Months  &lt;/div&gt; tag

because of a tag containing similar class:

&lt;div class="item_body" id="start-date-first"&gt;
     &lt;span class="start_immediately_mobile"&gt;Starts&nbsp;immediately&lt/span&gt

<b> Output:</b>
<br>
<textarea>
0.
Company_Name -> AgentInsights
Job_Role -> Computer Vision
Duration ->
Starts immediatelyImmediately
</textarea>
<br>
<b> Desired Output:</b>
<textarea>
0.
Company_Name -> AgentInsights
Job_Role -> Computer Vision
Duration -> 3 Months
</textarea>
</p>
<br>
Author- Richa Mishra
