import org.apache.http.*;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.message.BasicHeaderElementIterator;
import org.apache.http.message.BasicHttpResponse;

import java.io.IOException;

/**
 * Created by wbshi on 2016/3/24 0024.
 */
public class SimpleRequest {
    public static  void main(String args[]) {
        HttpResponse response = new BasicHttpResponse(HttpVersion.HTTP_1_1, HttpStatus.SC_OK, "OK");
        response.addHeader("Set-Cookie", "c1=a; path=/; domain=localhost");
        response.addHeader("Set-Cookie", "c2=b; path=\"/\",c3=c, domain=\"localhost\"");
        Header header1 = response.getFirstHeader("Set-Cookie");
        System.out.println(header1);
        Header header2 = response.getLastHeader("Set-Cookie");
        System.out.println(header2);

        HeaderElementIterator elementIterator = new BasicHeaderElementIterator(response.headerIterator("Set-Cookie"));
        while (elementIterator.hasNext()) {
            HeaderElement element = elementIterator.nextElement();
            System.out.println(element.getName() + "=" + element.getValue());
            NameValuePair[] params = element.getParameters();
            for(int i=0; i<params.length; i++) {
                System.out.println(params[i].getName() + "=" + params[i].getValue());
            }

        }

    }
}
