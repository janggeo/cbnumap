package com.map_project.map;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Build;
import android.os.Bundle;
import android.view.KeyEvent;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends AppCompatActivity  {
 private WebView web;
 @Override
 protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);
  setContentView(com.example.map.R.layout.activity_main);
  web = (WebView) findViewById(com.example.map.R.id.webView);
  /* 웹 세팅 작업하기 */
  WebSettings webSettings = web.getSettings();
  webSettings.setJavaScriptEnabled(true);
  webSettings.setDomStorageEnabled(true);
  webSettings.setJavaScriptCanOpenWindowsAutomatically(false);
  webSettings.setAllowFileAccessFromFileURLs(true);
  webSettings.setAllowUniversalAccessFromFileURLs(true);
  webSettings.setSupportMultipleWindows(false);//true로 하면 라이브리 로그인 안됨.
  webSettings.setUseWideViewPort(true);  //html 컨텐츠가 웹뷰에 맞게 나타남
  webSettings.setLoadWithOverviewMode(true);
  webSettings.setSaveFormData(true);

  web.setWebViewClient(new WebViewClient());
  web.setWebChromeClient(new WebChromeClient());

  if(Build.VERSION.SDK_INT >= 21) {
   webSettings.setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW);
  }
  web.loadUrl("https://jazzy-churros-c02313.netlify.app/");
 }
 @Override
 public boolean onKeyDown(int keyCode, KeyEvent event) {
  if (keyCode == KeyEvent.KEYCODE_BACK) {
   if (web.canGoBack()) {
    web.goBack();
    return false;
   }
  }
  return super.onKeyDown(keyCode, event);
 }
}