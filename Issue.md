<title> Extracting data from tags containing similar class type </title>


<p>
I am facing a problem in obtaining the data for the duration of Internship from the below mentioned tag:

&ltdiv class="item_body"&gt 3 Months  &lt/div&gt tag

because of a tag containing similar class:

&ltdiv class="item_body" id="start-date-first"&gt
     &ltspan class="start_immediately_mobile"&gtStarts&nbsp;immediately&lt/span&gt

<b> Output:</b>

0.
Company_Name -> AgentInsights
Job_Role -> Computer Vision
Duration ->
Starts immediatelyImmediately

<b> Desired Output:</b>

0.
Company_Name -> AgentInsights
Job_Role -> Computer Vision
Duration -> 3 Months
</p>
<br>
Author- Richa Mishra
