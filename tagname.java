package com;
import org.openqa.selenium.By;
import org.openqa.selenium.Platform;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.firefox.FirefoxDriver;
public class tagname {
    static String driverPath="D:\\geckodriver.exe";
    static  WebDriver driver;
    public static void main(String[] args){
        System.setProperty(" ", driverPath);
        DesiredCapabilities capabilities=new DesiredCapabilities();
        capabilities=DesiredCapabilities.firefox();
        capabilities.setBrowserName("firefox");
        capabilities.setVersion("38.0.5");
        capabilities.setPlatform(Platform.WINDOWS);
        capabilities.setCapability("", false);
        driver= new FirefoxDriver(capabilities);
        driver.get("http://toolsqa.com");
        java.util.List<WebElement>x=driver.findElements(By.tagName("a"));
        System.out.println("Total links are "+x.size());
        for(int i=0;i<x.size();i=i+1)
        {
            System.out.println("link "+i+" link name:-"+x.get(i).getText());
        }
    }
}
    