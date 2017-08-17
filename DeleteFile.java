package deletefile;

import java.io.File;

public class DeleteFile {
    public static void main(String[] args) {

        String files; 
        File file = new File("D:\\del");
        File[] listOfFiles = file.listFiles(); 
        for (int i = 0; i < listOfFiles.length; i++) 
        {
            if (listOfFiles[i].isFile()) 
            {
                files = listOfFiles[i].getName();
                System.out.println(files);
                if(!files.equalsIgnoreCase("Scan.pdf"))
                {
                    boolean issuccess=new File(listOfFiles[i].toString()).delete();
                    System.err.println("Deletion Success "+issuccess);
                }
            }
        }
    }
}