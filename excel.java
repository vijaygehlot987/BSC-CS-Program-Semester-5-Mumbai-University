
package excelwrite;
import jxl.Workbook;
import jxl.write.*;
import java.io.File;
public class excel {

    static final String Filelocation= "D:\\CreateExcel.xls";

    public static void main(String[] args) {
        WritableWorkbook workbook = null;
        try {
            workbook = Workbook.createWorkbook(new File(Filelocation));
            WritableSheet excelSheet = workbook.createSheet("Sheet 1", 0);
            Label label = new Label(0, 0, "Number");
            excelSheet.addCell(label);
            label = new Label(0, 1, "100");
            excelSheet.addCell(label);
            
            workbook.write();
        } catch (Exception e) {}
        finally {
            if (workbook != null) {
                try {
                    workbook.close();
                } catch (Exception e) {
                }}}}}