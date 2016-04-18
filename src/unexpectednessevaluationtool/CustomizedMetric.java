/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package unexpectednessevaluationtool;

/**
 *
 * @author labpi
 */
public class CustomizedMetric {
    
    /*
    Attributes, code, title and description
    */
    private String code;
    private String title;
    private String execution;

    /*
    Constructor
    */
    public CustomizedMetric() {
        this.code = "";
        this.title = "";
        this.execution = "";
    }

    /*
    Set the code 
    */
    public void setCode(String code) {
        this.code = code;
    }

    /*
    Set the title
    */
    public void setTitle(String title) {
        this.title = title;
    }

    /*
    Set the Execution
    */
    public void setExecution(String execution) {
        this.execution = execution;
    }
    
    
}
