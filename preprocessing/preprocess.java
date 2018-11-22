import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.BufferedReader;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileReader;
import java.io.IOException; 
import java.io.*;
import java.util.*;

public class preprocess{


    public static void main( String args[] ) {
        String myWholeFile = null;
        ArrayList<String> fName = new ArrayList<String>();
      fName.add("Twitter");
      fName.add("Facebook");
      fName.add("WhatsApp");
        for(int i = 0 ; i < 3 ;i++)
        {
          try {
         String name = "zero" + fName.get(i) + ".txt";   
         File file = new File(name);
         FileReader fileReader = new FileReader(file);
         BufferedReader bufferedReader = new BufferedReader(fileReader);
         StringBuffer stringBuffer = new StringBuffer();
         String line;
         name = "new" + fName.get(i) + ".txt";
        PrintWriter writer = new PrintWriter(name, "UTF-8");
         //PrintWriter writer1 = new PrintWriter("fb.txt", "UTF-8");



         while ((line = bufferedReader.readLine()) != null) {
             String newline ;
            
             String find = "([^a-zA-Z0-9\\s*])";
             String find2 = "[\\n]";
            // String x = find +  "|" + find2;
             Pattern p = Pattern.compile(find);
             Matcher m = p.matcher(line);
             while(m.find()){
                // System.out.println(line);
                 //System.out.println(m.group(0));
              //   char[] n = m.group(0).toCharArray(); 
                // if(n[0] == '\n')
                // {
                 //       System.out.println(n[0]);
                // }
                // else
                System.out.println(line);
                 line ="";
             }


         //    find = "https://(.)*";
           //  p = Pattern.compile(find);
           //  m = p.matcher(line);
            //              while(m.find()){
                // System.out.println(line);
                 //System.out.println(m.group(0));
           //      line ="";
            // }

             
            // System.out.println(line);

            if(line.equals(""))
            {

            }
            else{
                writer.println(line);
            }


            stringBuffer.append(line);
            stringBuffer.append("\n");
         }





         fileReader.close();
        writer.close();
         myWholeFile = stringBuffer.toString();
            } 
            catch (IOException e) {
         e.printStackTrace();


      }

     // System.out.println(myWholeFile);



  }
    }
}