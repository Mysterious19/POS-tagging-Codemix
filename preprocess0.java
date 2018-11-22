import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.BufferedReader;
import java.io.File;
import java.io.PrintWriter;
import java.io.FileReader;
import java.io.IOException; 
import java.io.*;
import java.util.*;

public class preprocess0{


    public static void main( String args[] ) {
        String myWholeFile = null;
      ArrayList<String> fName = new ArrayList<String>();
      fName.add("Twitter");
      fName.add("Facebook");
      fName.add("WhatsApp");
      for(int i=0;i<3;i++)
      {
          try {
        String name = fName.get(i) + ".txt";
         File file = new File(name);
         FileReader fileReader = new FileReader(file);
         BufferedReader bufferedReader = new BufferedReader(fileReader);
         StringBuffer stringBuffer = new StringBuffer();
         String line;
         name = "zero" + fName.get(i) + ".txt";

		File fw = new File(name);
        FileWriter writer = new FileWriter(fw);
        // PrintWriter writer1 = new PrintWriter("zerofb.txt", "UTF-8");
		int li = 0;
        while ((line = bufferedReader.readLine()) != null) {
           if(line.equals(""))
            {
                line = "0";
            }

           System.out.println(li++);
           writer.write(line + "\n");
         


           

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
