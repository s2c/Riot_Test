#include <curl/curl.h>
#include <stdio.h>
#include <iostream>
using namespace std ;

int main(int argc, char const *argv[]) {
 CURL *curl;
 CURLcode res;

 curl = curl_easy_init();

 if(curl) {
  /* First set the URL that is about to receive our POST. This URL can
     just as well be a https:// URL if that is what should receive the
     data. */
  curl_easy_setopt(curl, CURLOPT_URL, "https://www.google.co.uk");

  /* Perform the request, res will get the return code */
  res = curl_easy_perform(curl);

/* always cleanup */
  curl_easy_cleanup(curl);
}
 string key = "a0783aee-cba4-49fd-9013-80c51a035899";
 std::cout << key << std::endl;
  return 0;
}
