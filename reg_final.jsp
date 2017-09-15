<%@ page language="java" contentType="text/html; charset=utf-8"%>

 

<!-- 파일 업로드 처리를 위한 MultipartRequest 객체를 임포트 -->

<%@ page import="com.oreilly.servlet.MultipartRequest" %> 

 

<!-- 파일 중복처리 객체 임포트 -->

<%@ page import="com.oreilly.servlet.multipart.DefaultFileRenamePolicy" %> 

 

<%@ page import="java.util.*" %>
<%@ page import="java.io.*" %>
<%@ page import="java.text.*" %>

<%

 String uploadPath = "D:\\Python\\Scripts\\images\\input_test\\";

 

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
  if (fileName1 == null) {
	  fileName1 =  "null";
  } else {
	  Random generator = new Random();
	  int num1 = generator.nextInt();
	  int index = fileName1.indexOf(".");
	  String newFileName = fileName1.substring(index, fileName1.length());
	  String now = new SimpleDateFormat("yyyMMddHmsS").format(new Date());
	  String newFile = now + num1 + newFileName;
	  
	  File file = new File(uploadPath+"/"+fileName1);
	  file.renameTo(new File(uploadPath+"/"+newFile));
	  fileName1 = newFile;
  }
  
  //String file2 = (String)files.nextElement();
  //fileName1 = multi.getFilesystemName(file2);
  fileName2 = multi.getFilesystemName("fileName2");
  //originalName1 = multi.getOriginalFileName(file2);
  originalName2 = multi.getOriginalFileName("fileName2");
  if (fileName2 == null) {
	  fileName2 =  "null";
  } else {
	  Random generator = new Random();
	  int num1 = generator.nextInt();
	  int index = fileName2.indexOf(".");
	  String newFileName = fileName2.substring(index, fileName2.length());
	  String now = new SimpleDateFormat("yyyMMddHmsS").format(new Date());
	  String newFile = now + num1 + newFileName;
	  
	  File file = new File(uploadPath+"/"+fileName2);
	  file.renameTo(new File(uploadPath+"/"+newFile));
	  fileName2 = newFile;
  }
  //String file3 = (String)files.nextElement();
  //fileName3 = multi.getFilesystemName(file3);
  fileName3 = multi.getFilesystemName("fileName3");
  //originalName3 = multi.getOriginalFileName(file3);
  originalName3 = multi.getOriginalFileName("fileName3");
  if (fileName3 == null) {
	  fileName3 =  "null";
  } else {
	  Random generator = new Random();
	  int num1 = generator.nextInt();
	  int index = fileName3.indexOf(".");
	  String newFileName = fileName3.substring(index, fileName3.length());
	  String now = new SimpleDateFormat("yyyMMddHmsS").format(new Date());
	  String newFile = now + num1 + newFileName;
	  
	  File file = new File(uploadPath+"/"+fileName3);
	  file.renameTo(new File(uploadPath+"/"+newFile));
	  fileName3 = newFile;
  }  
 }catch(Exception e){
  e.printStackTrace();

 }
String result = "";
String warning = "";
String hospital = "";
 try {
	 ProcessBuilder pb = new ProcessBuilder("C:\\Users\\user\\Anaconda3\\python","D:\\Python\\Scripts\\test_fix.py", fileName1,fileName2,fileName3);
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
		 if(line.contains("확인")) {
			 warning = line;
		 }
		 if(line.contains("병원")) {
			 hospital = line;
		 }
		 
		 
	     System.out.println("Python Output: " + line);
	 }
	 System.out.println("........end   process......."); 
 } catch(Exception e){
	  e.printStackTrace();

	 }


%>

  

<html>
<head>
<meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="generator" content="Mobirise v4.2.0, mobirise.com">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="shortcut icon" href="assets/images/brain-250x217.png" type="image/x-icon">
  <meta name="description" content="">
  <title>Brain</title>
  <link rel="stylesheet" href="assets/web/assets/mobirise-icons/mobirise-icons.css">
  <link rel="stylesheet" href="assets/tether/tether.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-grid.min.css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-reboot.min.css">
  <link rel="stylesheet" href="assets/socicon/css/styles.css">
  <link rel="stylesheet" href="assets/dropdown/css/style.css">
  <link rel="stylesheet" href="assets/theme/css/style.css">
  <link href="https://fonts.googleapis.com/css?family=Rubik:300,300i,400,400i,500,500i,700,700i,900,900i" rel="stylesheet">
  <link href="assets/fonts/style.css" rel="stylesheet">
  <link rel="stylesheet" href="assets/mobirise/css/mbr-additional.css" type="text/css">
  </head>
<body>
<section class="menu cid-qtbfLwbL3T" once="menu" id="menu1-g" data-rv-view="131">

    

    <nav class="navbar navbar-expand beta-menu navbar-dropdown align-items-center navbar-fixed-top navbar-toggleable-sm">
        <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <div class="hamburger">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
            </div>
        </button>
        <div class="menu-logo">
            <div class="navbar-brand">
                <span class="navbar-logo">
                    <a href="https://mobirise.com">
                         <img src="assets/images/brain-250x217.png" alt="Mobirise" title="" media-simple="true" style="height: 3.8rem;">
                    </a>
                </span>
                <span class="navbar-caption-wrap"><a class="navbar-caption text-white display-5" href="https://mobirise.com">&nbsp;빅데이터 청년인재&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; project&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</a></span>
            </div>
        </div>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav nav-dropdown nav-right" data-app-modern-menu="true"><li class="nav-item">
                    <a class="nav-link link text-white display-4" href="https://mobirise.com">
                        <span class="mbri-home mbr-iconfont mbr-iconfont-btn"></span>&nbsp;Home &nbsp;</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link link text-white display-4" href="http://13.124.5.168:8080/brain/index.jsp">
                        <span class="mbri-search mbr-iconfont mbr-iconfont-btn"></span>&nbsp;Contact Us
                    </a>
                </li></ul>
            
        </div>
    </nav>
</section>

<section class="engine"><a href="https://mobirise.co/q">bootstrap slider</a></section><section class="cid-qtbfLxly1C mbr-fullscreen mbr-parallax-background" id="header2-e" data-rv-view="133">

    

    

    <div class="container align-center">
        <div class="row justify-content-md-center">
            <div class="mbr-white col-md-10">
                <h1 class="mbr-section-title mbr-bold pb-3 mbr-fonts-style display-1"><%=result%>
                </h1>
                <br>
                <p class="mbr-text pb-3 mbr-fonts-style display-5"><%=hospital%><%=warning%><br></p>
        </div>
    </div>
    
</section>

<section class="cid-qtbfLy3X5U" id="footer1-f" data-rv-view="136">

    

    

    <div class="container">
        <div class="media-container-row content text-white">
            <div class="col-12 col-md-3">
                <div class="media-wrap">
                    <a href="https://mobirise.com/">
                        <img src="assets/images/brain-250x217.png" alt="Mobirise" title="" media-simple="true">
                    </a>
                </div>
            </div>
            <div class="col-12 col-md-3 mbr-fonts-style display-7">
                <h5 class="pb-3">
                    Address
                </h5>
                <p class="mbr-text">부산 금정구 부산대학로63번길 &nbsp;<br>부산대학교자연대연구실험동</p>
            </div>
            <div class="col-12 col-md-3 mbr-fonts-style display-7">
                <h5 class="pb-3">
                    Contacts
                </h5>
                <p class="mbr-text">문필준, 송민재, 고유정, 김유미&nbsp;<br>Phone: +4 (0) 000 0000 001
<br></p>
            </div>
            <div class="col-12 col-md-3 mbr-fonts-style display-7">
                <h5 class="pb-3">
                    Links
                </h5>
                <p class="mbr-text">
                    <a class="text-primary" href="https://mobirise.com/">Website builder</a>
                    <br><a class="text-primary" href="https://mobirise.com/mobirise-free-win.zip">Download for Windows</a>
                    <br><a class="text-primary" href="https://mobirise.com/mobirise-free-mac.zip">Download for Mac</a>
                </p>
            </div>
        </div>
        <div class="footer-lower">
            <div class="media-container-row">
                <div class="col-sm-12">
                    <hr>
                </div>
            </div>
            <div class="media-container-row mbr-white">
                <div class="col-sm-6 copyright">
                    <p class="mbr-text mbr-fonts-style display-7">
                        © Copyright 2017 Mobirise - All Rights Reserved
                    </p>
                </div>
                <div class="col-md-6">
                    <div class="social-list align-right">
                        <div class="soc-item">
                            <a href="https://twitter.com/mobirise" target="_blank">
                                <span class="socicon-twitter socicon mbr-iconfont mbr-iconfont-social" media-simple="true"></span>
                            </a>
                        </div>
                        <div class="soc-item">
                            <a href="https://www.facebook.com/pages/Mobirise/1616226671953247" target="_blank">
                                <span class="socicon-facebook socicon mbr-iconfont mbr-iconfont-social" media-simple="true"></span>
                            </a>
                        </div>
                        <div class="soc-item">
                            <a href="https://www.youtube.com/c/mobirise" target="_blank">
                                <span class="socicon-youtube socicon mbr-iconfont mbr-iconfont-social" media-simple="true"></span>
                            </a>
                        </div>
                        <div class="soc-item">
                            <a href="https://instagram.com/mobirise" target="_blank">
                                <span class="socicon-instagram socicon mbr-iconfont mbr-iconfont-social" media-simple="true"></span>
                            </a>
                        </div>
                        <div class="soc-item">
                            <a href="https://plus.google.com/u/0/+Mobirise" target="_blank">
                                <span class="socicon-googleplus socicon mbr-iconfont mbr-iconfont-social" media-simple="true"></span>
                            </a>
                        </div>
                        <div class="soc-item">
                            <a href="https://www.behance.net/Mobirise" target="_blank">
                                <span class="socicon-behance socicon mbr-iconfont mbr-iconfont-social" media-simple="true"></span>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>



</body>

</html>