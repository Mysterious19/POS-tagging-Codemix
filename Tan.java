import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException; 
import java.io.*;
import java.util.*;

public class Tan {

 
   public static void main( String args[] ) {
      String myWholeFile = null;
      ArrayList<String> file_data = new ArrayList<String>();
      try {
           //name = "new" + fName.get(i) + ".txt";
         File file = new File("newWhatsApp.txt");
         FileReader fileReader = new FileReader(file);
         BufferedReader bufferedReader = new BufferedReader(fileReader);
         StringBuffer stringBuffer = new StringBuffer();
         String line;
        
         while ((line = bufferedReader.readLine()) != null) {
          file_data.add(line);
            stringBuffer.append(line);
            stringBuffer.append("\n");
         }
         fileReader.close();
       
         myWholeFile = stringBuffer.toString();
            } 
            catch (IOException e) {
         e.printStackTrace();
      }
      
     
      
      try{

      int j;
         // name = "new" + fName.get(i) + "_line.txt";
          //File file = new File(name);
          PrintWriter fw = new PrintWriter("WaData.txt","UTF-8");
          for( j =0 ;j<file_data.size();j++ )
          {
            if(file_data.get(j).equals("0"))
            {
              //fw.write( "\n");
              fw.println();
            }
            else
            {
              fw.println(file_data.get(j));
              //fw.write(file_data.get(i) +"\n");
            }

          }
          fw.close();

    }
    catch(IOException e)
    {
      e.printStackTrace();
    }
    }
  }
