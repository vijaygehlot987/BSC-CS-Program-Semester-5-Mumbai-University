package prac6testing;
import java.io.File;
import java.io.IOException;
import jxl.Cell;
import jxl.CellType;
import jxl.Sheet;
import jxl.Workbook;
public class retrievelExcel {
    public static void read()throws IOException{
        File inputWorkBook= new File("C://Users//Vijay//Documents//prac5st//sample.xsl");
        Workbook w;
        boolean flag=false;
        int count=0;
        try{
            w=Workbook.getWorkbook(inputWorkBook);
            Sheet sheet=w.getSheet(0);
            for(int j =0;j<sheet.getRows();j++){
            Cell cell=sheet.getCell(4, j);
            if(cell.getType()==CellType.NUMBER)
                if(Integer.parseInt(cell.getContents())>100){
                    count++;}
            }
            System.out.println("Total number of students who scored more than 100 is    "+ count++);
        }
        catch (Exception e){}
    }
   
     // @param args the command line arguments
     
    public static void main(String[] args)throws IOException {
        // TODO code application logic here
        read();
    }
    
}
