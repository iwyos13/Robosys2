# Robosys2<br>
授業内容<br>
ROSの起動からパブリッシャ(送信)とサブスクライバ(受信)の製作, 実行まで<br>

(Tera Term でROSを行う場合, ROS実行画面, プログラム実行画面, CUI画面の ３個を起動する必要がある)<br>
 (例. Roscore, xxx.py, CUI)<br>
 
ROSの起動:roscore<br>
パブリッシャの作成(数字をカウントしていくプログラム)<br>
count.py<br>
サブスクライバの作成(count.pyの値を読み取り,2倍にして表示)<br>
twice.py<br>

プログラムの実行<br>
$:chmod a+x mypkg count.py (count.py に管理者権限を付与)<br>
$:rosrun mypkg count.py<br>
実行の確認<br>
rostopic echo /count_up <br>





作成したプログラム<br>
詳細はpackage.xmlに記載<br>


kadaip.py , kadais.py,<br>
どちらともcount.py, twice.pyの改良<br>


kadaip.py<br>

rate = を20Hzにすることにより、一秒につき20回動作<br>
n += 5 に変更<br>

kadais.py<br>
受け取ったcount_upの値+1 を行い,この値×3 を表示する<br>
