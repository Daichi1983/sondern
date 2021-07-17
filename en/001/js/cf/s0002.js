<script>

//キー押下時に関数pageMove()を呼び出す
document.onkeydown = pageMove;
var ue, mae, ato;

ue = "l001-l002/";
mae = "s0001/";
ato = "s0003/";

function pageMove()
{
  if (event.keyCode == 37)  //「←」が押されたか確認
  {
    location.href = mae;
  }
  if (event.keyCode == 38)  //「↑」が押されたか確認
  {
    location.href = ue;
  }
  if (event.keyCode == 39)  //「→」が押されたか確認
  {
    location.href = ato;
  }
}

</script>

<div class="tab_change">
  <!-- タブボタン部分 -->
  <ul class="nav nav-tabs" style="list-style: none;">
    <li class="nav-item">
      <a href="#tab1" class="nav-link active" data-toggle="tab">翻刻</a>
    </li>
    <li class="nav-item">
      <a href="#tab2" class="nav-link" data-toggle="tab">原本 | Original</a>
    </li>
    <li class="nav-item">
      <a href="#tab3" class="nav-link" data-toggle="tab">English</a>
    </li>
  </ul>
  <!--タブのコンテンツ部分-->
  <div class="tab-content">
    <div id="tab1" class="tab-pane active">

<h2>名詞 固有名詞</h2>
<p>12. ging Deutschlandの問題は形容の●●●●●●●<br>13.「誰彼」の意に任意の固有名詞を用ふ<br>－指示用</p>
<ol>
<li>固有の［1］</li>
<li>Theseus' Stadt等は「名詞、各変化」</li>
<li>不定冠詞の場合は不定冠詞の項</li>
<li>ein Davinci等</li>
<li>Durch das Hessische等</li>
<li>固有名と定冠詞（地名、人名）</li>
<li>à la Kaiserの問題も加ふ可し。</li>
<li>mendeln, marsen等、動詞</li>
<li>「ein Bechstein m, ピヤノ」等は「性數」</li>
<li>固有名として普通名を假に用ひる場合<br>（Freund Hain等の項）（Drei Käsehah等）</li>
<li>固有人名のpl.は複數の冊</li>
</ol>
<br><br><a href="#" onclick="javascript:window.history.back(-1);return false;">Back</a>

    </div>
    <div id="tab2" class="tab-pane">

<p><a href="http://biblevi.minibird.jp/sekiguchi/wp-content/uploads/2018/10/S0002.gif"><img id="exifviewer-img-1" class="alignnone size-large wp-image-117" src="http://biblevi.minibird.jp/sekiguchi/wp-content/uploads/2018/10/S0002-725x1024.gif" alt="" width="725" height="1024"></a></p>
<br><br><a href="#" onclick="javascript:window.history.back(-1);return false;">Back</a>


    </div>
    <div id="tab3" class="tab-pane">

<h2>Noun Proper Noun</h2>
<p>12. Problem of ging Deutschland is in Description of *****<br>13.Use a proper noun as a meaning of "someone"<br>- for an indication</p>
<ol>
<li>[1] of unique</li>
<li>Theseus' Stadt etc. is in "Noun, each Changes"</li>
<li>In case of the indefinite article, refer to items of "Indifinite Article"</li>
<li>ein Davinci etc.</li>
<li>Durch das Hessische etc.</li>
<li>Proper Name and Definite Article (Name of Place, People)</li>
<li>must add the problem of à la Kaiser</li>
<li>mendeln, marsen etc., Verb</li>
<li>"ein Bechstein m, Piano" etc. are in "Sex and Number"</li>
<li>In case of tentative usage of a normal name as a proper name<br>(Item of Freund Hain etc.) (Drei Käsehah etc.)</li>
<li>pl. of proper noun is in the book of "Plural".</li>
</ol>
<br><br><a href="#" onclick="javascript:window.history.back(-1);return false;">Back</a>

    </div>
  </div>
</div>