<%
dim name,location,class
name=Request.Form("name")
location=Request.Form("location")
class=Request.Form("class")
$output = array(name, location, class);
echo $output
%>
