package Softwaretesting8;
import org.openqa.selenium.By;
import org.openqa.selenium.Platform;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.firefox.FirefoxDriver;

public class xpath {
    static String driverPath="C://geckodriver";
    static WebDriver driver;
    public static void main(String[] args){
        System.setProperty("abc", driverPath);
        DesiredCapabilities capabilities=new DesiredCapabilities();
        capabilities=DesiredCapabilities.firefox();
        capabilities.setBrowserName("firefox");
        capabilities.setVersion("38.0.5");
        capabilities.setPlatform(Platform.WINDOWS);
        capabilities.setCapability("marionette", false);
        driver= new FirefoxDriver(capabilities);
        driver.get("C:\\City.html");
        java.util.List<WebElement>x=driver.findElements(By.xpath("//select/option"));
        System.out.println("No. of City/cities in the combobox is/are "+x.size());
        for(int i=0;i<x.size();i++)
        {
            System.out.println("City Name:-"+x.get(i).getText());
        }
    }
}
    