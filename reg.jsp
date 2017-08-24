<%@ page language="java" contentType="text/html; charset=utf-8"%>

 

<!-- 파일 업로드 처리를 위한 MultipartRequest 객체를 임포트 -->

<%@ page import="com.oreilly.servlet.MultipartRequest" %> 

 

<!-- 파일 중복처리 객체 임포트 -->

<%@ page import="com.oreilly.servlet.multipart.DefaultFileRenamePolicy" %> 

 

<%@ page import="java.util.*" %>
<%@ page import="java.io.*" %>
 

<%

 String uploadPath = "E:\\Python\\Scripts\\images\\input_test\\";

 

//업로드 파일 최대 크기 지정

 int size = 10*1024*1024;        
 String name = "";
 String subject = "";
 String fileName1 = "";
 String originalName1 = "";
 String fileName2 = "";
 String originalName2 = "";
 String fileName3 = "";
 String originalName3 = "";
 
 MultipartRequest multi = null;
 try{

  // 파일 업로드. 폼에서 가져온 인자값을 얻기 위해request 객체 전달, 업로드 경로, 파일 최대 크기, 한글처리, 파일 중복처리

	multi = new MultipartRequest(request, uploadPath, size, "utf-8", new DefaultFileRenamePolicy());
	  // 파일 업로드. 폼에서 가져온 인자값을 얻기 위해request 객체 전달, 업로드 경로, 파일 최대 크기, 한글처리, 파일 중복처리
  Enumeration files = multi.getFileNames(); 
  //String file1 = (String)files.nextElement();
  //fileName2 = multi.getFilesystemName(file1);
  fileName1 = multi.getFilesystemName("fileName1");
  //originalName2 = multi.getOriginalFileName(file1);
  originalName1 = multi.getOriginalFileName("fileName1");
  
  
  //String file2 = (String)files.nextElement();
  //fileName1 = multi.getFilesystemName(file2);
  fileName2 = multi.getFilesystemName("fileName2");
  //originalName1 = multi.getOriginalFileName(file2);
  originalName2 = multi.getOriginalFileName("fileName2");
  if (fileName2 == null) {
	  fileName2 =  "null";
  }
  
  //String file3 = (String)files.nextElement();
  //fileName3 = multi.getFilesystemName(file3);
  fileName3 = multi.getFilesystemName("fileName3");
  //originalName3 = multi.getOriginalFileName(file3);
  originalName3 = multi.getOriginalFileName("fileName3");
  if (fileName3 == null) {
	  fileName3 =  "null";
  }
 }catch(Exception e){
  e.printStackTrace();

 }
String result = "";
String warning1 = "";
String warning2 = "";
String warning3 = "";
 try {
	 ProcessBuilder pb = new ProcessBuilder("E:\\anaconda\\python","E:\\Python\\Scripts\\test_fix.py", fileName1,fileName2,fileName3);
	 pb.redirectErrorStream(true);
	 Process p = pb.start();
	 BufferedReader bfr = new BufferedReader(new InputStreamReader(p.getInputStream()));
	 String line = "";
	 System.out.println(".........start   process.........");
	 line = bfr.readLine();
	 //    line = bfr.readLine();
	 while ((line = bfr.readLine()) != null) {
		 if(line.contains("!")) {
			 result = line;
		 }
		 if(line.contains("1번")) {
			 warning1 = line;
		 }
		 if(line.contains("2번")) {
			 warning1 = line;
		 }
		 if(line.contains("3번")) {
			 warning1 = line;
		 }
	     System.out.println("Python Output: " + line);
	 }
	 System.out.println("........end   process......."); 
 } catch(Exception e){
	  e.printStackTrace();

	 }



%>

  

<html>

<body>

<%=result %>
<%=warning1 %>
<%=warning2 %>
<%=warning3 %>
</body>

</html>
