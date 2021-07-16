<script>

//キー押下時に関数pageMove()を呼び出す
document.onkeydown = pageMove;
var ue, mae, ato;

ue = "l001-l002/";
mae = "l001-l002/";
ato = "s0002/";

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

<h2>固有名詞でもあり普通名詞でもあり:</h2>
<ol>
<li>平原名（地理）→</li>
<li>帝王名</li>
<li>風名</li>
<li>人名</li>
</ol>
<h2 style="margin-top: 2em;">平原</h2>
<p>Die Pampas. Die Llianos. Die Steppe. Tundra, -en. Wüste,</p>
<ol>
<li>Die Gauchos reiten tagelang über die <u>Llianos</u>.<br>南米アマゾン以北の平原</li>
</ol>
<p>ヤノス（中）<br>ジャノス（南）<br>リャノス（北）</p>

<br><br><a href="#" onclick="javascript:window.history.back(-1);return false;">Back</a>

    </div>
    <div id="tab2" class="tab-pane">
      <p><a href="http://biblevi.minibird.jp/sekiguchi/wp-content/uploads/2018/10/S0001.gif"><img class="alignnone size-large wp-image-116" src="http://biblevi.minibird.jp/sekiguchi/wp-content/uploads/2018/10/S0001-725x1024.gif" alt="" width="725" height="1024"></a></p>
<br><br><a href="#" onclick="javascript:window.history.back(-1);return false;">Back</a>

    </div>
    <div id="tab3" class="tab-pane">

<h2>At once proper noun and normal noun:</h2>
<ol>
<li>Name of Plain (geometry) →</li>
<li>Name of Emperor</li>
<li>Name of Wind</li>
<li>Name of People</li>
</ol>
<h2 style="margin-top: 2em;">Plain</h2>
<p>Die Pampas. Die Llianos. Die Steppe. Tundra, -en. Wüste,</p>
<ol>
<li>Die Gauchos reiten tagelang über die <u>Llianos</u>.<br>The plain located in the northern part of the Amazon</li>
</ol>
<p>[yanos] (mid.)<br>[janos] (south)<br>[lyanos] (north)</p><br><br><a href="#" onclick="javascript:window.history.back(-1);return false;">Back</a>

    </div>
  </div>
</div>