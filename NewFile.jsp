<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<%@ page import="java.io.*" %>
<%@ page import="java.util.*" %>

<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
<title>Insert title here</title>
</head>
<%
String line="";

try{
    ProcessBuilder pb = new ProcessBuilder("C:\\Python27\\python.exe","E:\\a.py");
    pb.redirectErrorStream(true);
    Process p = pb.start();
    
    
    BufferedReader bfr = new BufferedReader(new InputStreamReader(p.getInputStream()));

    System.out.println(".........start   process.........");  
    
 
        line = bfr.readLine();
    

    System.out.println("........end   process.......");

    }catch(Exception e){System.out.println(e);}


%>
<body>
<%= line  %>
</body>
</html>