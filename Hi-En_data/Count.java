import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException; 
import java.io.*;
import java.util.*;

public class Count{

 
   public static void main( String args[] ) {
      String myWholeFile = null;
      ArrayList<String> fName = new ArrayList<String>();
      fName.add("Twitter");
      fName.add("Facebook");
      fName.add("WhatsApp");
      String name  = null;
      for(int i=0;i<3;i++)
      {
        name = fName.get(i) + ".txt";
      ArrayList<String> file_data = new ArrayList<String>();
      try {
        
          int hi=0,ne=0,en=0,uni=0;

         File file = new File(name);
         FileReader fileReader = new FileReader(file);
         BufferedReader bufferedReader = new BufferedReader(fileReader);
         StringBuffer stringBuffer = new StringBuffer();
         String line;
        

        HashMap<String,Integer> hm = new HashMap<String,Integer>();
         while ((line = bufferedReader.readLine()) != null) {
          file_data.add(line);
          String splitText[] = line.split("\\s+");
          if(splitText.length >= 3)
          {
            if(hm.containsKey(splitText[2])){
              hm.put(splitText[2],hm.get(splitText[2])+1);
            }
            else
              hm.put(splitText[2],1);
          
          if(splitText[1].equals("hi"))
            hi++;
          else if(splitText[1].equals("en"))
            en++;
          else if(splitText[1].equals("ne"))
            ne++;
          else
            uni++;
            stringBuffer.append(line);
            stringBuffer.append("\n");

          }

         }
         System.out.println(name);
          System.out.println("Hindi count is: " + hi);
          System.out.println("English count is: " + en);
          System.out.println("Universal count is: " + uni);
          System.out.println("Name entity count is: " + ne);
        int total = hi+ne+en+uni;
          System.out.println("total count is: " + total);
          System.out.println();
         

         Set set2 = hm.entrySet();
        Iterator iterator2 = set2.iterator();
        while(iterator2.hasNext()) {
          Map.Entry mentry2 = (Map.Entry)iterator2.next();
          System.out.print("Key is: "+mentry2.getKey() + " & Value is: ");
          System.out.println(mentry2.getValue());
       }

         fileReader.close();
       
         myWholeFile = stringBuffer.toString();
            } 
            catch (IOException e) {
         e.printStackTrace();
      }
      
    }
  }
  }
