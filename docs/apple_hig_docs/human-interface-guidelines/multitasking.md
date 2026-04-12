# マルチタスク

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/multitasking

# マルチタスク

マルチタスクを活用すると、あるアプリから別のアプリに素早く切り替えて、それぞれのタスクを行うことができます。

![分割ビューで並べて配置された2つのウインドウのスケッチ。マルチタスクを示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせるオレンジ色になっています。](https://docs-assets.developer.apple.com/published/c0aa39820372aed95f9670453687c22b/patterns-multitasking-intro%402x.png)

ユーザはデバイスでマルチタスクが行えることが当たり前であると思っているので、マルチタスクが使えないと、アプリに不具合があると考えるかもしれません。ゲームやフルスペースで実行するApple Vision Proアプリなど、ごく一部の例外を除き、すべてのアプリをマルチタスクに対応させる必要があります。

マルチタスクでは、アプリの切り替えだけでなく、それぞれのデバイスに応じた機能を表示できます。[プラットフォームの考慮事項](/jp/design/human-interface-guidelines/multitasking#Platform-considerations)を参照してください。

## [ベストプラクティス](/jp/design/human-interface-guidelines/multitasking#Best-practices)

優れたマルチタスク環境では、さまざまなコンテキストでコンテンツを同時に管理することで、複数のアプリでの作業を遂行することができます。ユーザがいつマルチタスクを始めるかは分からないので、アプリやゲームは常に現在の状態を保存して復元できるようにしておく必要があります。

**ユーザが別のアプリに切り替える際でも、ユーザの注意や積極的な関与が必要なアクティビティは一時停止しておく。** 例えば、ゲームやメディア視聴のアプリなら、ユーザが別のアプリに切り替えても何かを見逃してしまうことがないようにします。ユーザが復帰したときに、もとの状態から開始させて、切り替えを感じさせないようにしましょう。

**オーディオの中断にはスムーズに反応する。** 使用中のアプリのオーディオで、別のアプリやシステムのオーディオからの中断が発生することがあります。例えば、通話の着信やSiriで開始したミュージックプレイリストが、アプリのオーディオに割り込むことがあります。このようなことが起きた場合、ユーザはアプリが次の方法で応答することを期待します:

  * ミュージック、ポッドキャスト、オーディオブックの再生など重要なオーディオで中断が発生した場合は、無期限にオーディオを停止します。

  * GPSの方向通知などで短い中断が発生した場合は、一時的に音量を下げるかオーディオを中断し、割り込みが終了したときに元の音量に戻すか再生を再開します。

ガイダンスは、[オーディオの再生](/jp/design/human-interface-guidelines/playing-audio)を参照してください。

**ユーザが開始したタスクは、バックグラウンドで完了させる。** アセットのダウンロードやビデオファイルの処理などのタスクを開始してから別のアプリに切り替えた場合、ユーザは開始したタスクが完了するものと期待します。アプリで処理中のタスクが追加の入力を必要としない場合は、サスペンドする前にバックグラウンドでタスクを完了するようにしてください。

**通知は控えめにする。** アプリがサスペンドした場合やバックグラウンドで実行されている場合でも、通知を送ることができます。ユーザが重要なタスクや緊急で実行しなければならないタスクを開始してからアプリを切り替えた場合、タスクが完了したときに通知を受け取れるとよいかもしれません。それにより、アプリに戻って次の手順に進むことができます。逆に、日常的なタスクやあまり重要でないタスクが完了した場合、通常はすぐにそれを知る必要はありません。このようなシナリオでは、不要な通知は送らないようにし、ユーザがアプリに戻ったときにタスクを確認できるようにしてください。ガイダンスは、[通知の管理](/jp/design/human-interface-guidelines/managing-notifications)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/multitasking#Platform-considerations)

 _watchOSには対応していません。_

### [iOS](/jp/design/human-interface-guidelines/multitasking#iOS)

iPhoneでマルチタスクを使用すると、ピクチャインピクチャでFaceTimeやビデオの視聴を行いながら、別のアプリを使用することができます。

![iPhoneのアプリスイッチャー。4つのアプリが開いています。](https://docs-assets.developer.apple.com/published/8e9bde3ae3602dd3fe2f3a1254c149df/multitasking-app-switcher-iphone%402x.png)

アプリスイッチャー。現在開いているすべてのアプリが表示されています。

![iPhoneの「メール」のスクリーンショット。個々のメールが表示されています。メール本文に重ねて、左下隅に現在FaceTime通話中の相手の小さな画像が表示されています。](https://docs-assets.developer.apple.com/published/f68005bf620706a5d6c6c03d09af37f4/multitasking-pip-iphone%402x.png)

現在のFaceTime通話を続けながら、別のアプリを使用することができます。

### [iPadOS](/jp/design/human-interface-guidelines/multitasking#iPadOS)

iPadでは、同時に複数のアプリの[ウインドウ](/jp/design/human-interface-guidelines/windows)を表示して操作できます。個々のアプリの中でも複数のウインドウを開いておけるので、ユーザは同じアプリで同時に複数のウインドウを表示して操作できます。

iPadでは、フルスクリーンまたはウインドウ表示でアプリを使用できます。フルスクリーンの場合、アプリはフルスクリーンで表示され、アプリスイッチャーを使用して個々のアプリウインドウを切り替えることができます。

![横向きのiPadのアプリスイッチャー。4つのアプリが開いています。アプリのサムネール表示がグリッド内に配置されています。](https://docs-assets.developer.apple.com/published/b80ea548dbb23308b1475a3f5d8e9882/multitasking-ipad-app-switcher%402x.png)

ウインドウ表示でアプリを使用するときは、アプリウインドウのサイズ変更が可能であり、macOSと同様の動作でニーズに合わせてウインドウを配置することができます。一般的なタイル表示構成、ウインドウのフルスクリーン表示、最小化、および閉じる操作を行うためのウインドウコントロールが用意されています。システムは、最前面のウインドウのウインドウコントロールを色付けし、その背後のウインドウにドロップシャドウを付けることで、最前面のウインドウを識別します。ガイダンスは、[「ウインドウ」＞「iPadOS」](/jp/design/human-interface-guidelines/windows#iPadOS)を参照してください。

![横向きのiPadの2つのウインドウ表示アプリのスクリーンショット。最前面のアプリウインドウは、その下にあるウインドウの上に重なって影を落としていて、色の付いたウインドウコントロールが、そのウインドウがアクティブであることを示しています。どちらのウインドウもホーム画面の背景の上に置かれていて、下部にDockが表示されています。](https://docs-assets.developer.apple.com/published/6a57b49307c4df279e34bee77f36949a/multitasking-ipad-windows-maps-landmarks%402x.png)

さらに、アプリがフルスクリーンでもウインドウ表示でも関係なく、ビデオやFaceTime通話は、ほかのコンテンツの上にピクチャインピクチャオーバーレイで再生することもできます。

注意

アプリでは、マルチタスク構成を制御したり、ユーザが選択する構成についての情報を受け取ったりすることはできません。

ユーザがウインドウ表示で開いたときにアプリが適切に応答できるように、さまざまな画面サイズにうまく適応するようにしてください。ガイダンスは[レイアウト](/jp/design/human-interface-guidelines/layout)および[ウインドウ](/jp/design/human-interface-guidelines/windows)を参照してください。デベロッパ向けのガイダンスは[iPad、Mac、Apple Vision Proでのマルチタスク](/documentation/UIKit/multitasking-on-ipad-mac-and-apple-vision-pro)を参照してください。iPadのマルチタスク機能をユーザがどのように使用するかについては、[iPadでマルチタスク機能を使う](https://support.apple.com/en-us/HT207582)を参照してください。

### [macOS](/jp/design/human-interface-guidelines/multitasking#macOS)

Macでは、同時に複数のアプリを実行し、ウインドウやタスクを切り替えながら作業するのが一般的なので、マルチタスクはデフォルトの体験です。複数のアプリウインドウを開いているときは、デスクトップ上でウインドウがレイヤーになっているように見える影が表示されるほか、ウインドウの状態を区別しやすくするためのその他のビジュアルエフェクトが適用されます。ガイダンスは[macOSのウインドウの状態](/jp/design/human-interface-guidelines/windows#macOS-window-states)を参照してください。

### [tvOS](/jp/design/human-interface-guidelines/multitasking#tvOS)

Apple TVでは、コンテンツを再生したり閲覧したりしながら、ピクチャインピクチャで映画やテレビ番組を再生することもできます（対応している場合）。

### [visionOS](/jp/design/human-interface-guidelines/multitasking#visionOS)

Apple Vision Proでは、共有スペースで複数のアプリを同時に実行し、空間内のウインドウやボリュームを切り替えながら閲覧することができます。

共有スペースでアクティブになるのは一度に1つのウインドウだけです。ユーザが1つのウインドウから視線を放して別のウインドウを見つめた場合は、現在見つめているウインドウがアクティブになりますが、以前のウインドウは透明度が増してz軸方向に後退したように見えます。共有スペースでアプリウインドウを閉じてもアプリは終了せず、単にバックグラウンドに移行します。

備考

アプリが「再生中」アプリの場合は、ウインドウを閉じるとオーディオの再生が自動的に一時停止します。再生を再開したい場合は、ウインドウを開くことなくコントロールセンターで再開できます。

**システムが提供するマルチタスクの動作を妨げない。** ユーザが1つのウインドウから別のウインドウを注視する場合は、視線を放したウインドウの状態の変化を明示するためにフェザー付きマスクが適用されます。この視覚的なフィードバックを妨げないようにするために、ウインドウのエッジの見た目は変化させないでください。

以下のカスタムコントロールを使用できます 

このビデオコンテンツの説明: visionOSの共有スペースにメモアプリと設定アプリが表示されている録画。ユーザがメモのウインドウの位置を変えて、少し設定のウインドウに重なるようにしてから、設定をアクティブ化し、そのあとにメモに戻っています。アプリがアクティブになるたびに、アクティブでなくなったアプリのウインドウにフェザーが適用されます。 

再生 

**視線を放したときにウインドウのビデオ再生が一時停止しないようにする。** 1つのウインドウで再生を開始したら、別のウインドウを閲覧したり別のウインドウでタスクを実行している間も再生は止まらないというのが、ユーザの期待する動作です。これは、macOSだけでなくvisionOSでも同様です。

**オーディオの音量が自動的に下がるケースに備える。** 「再生中」アプリ以外のアプリでは、ユーザが別のアプリに視線をそらしたときにオーディオがダッキングされます（オーディオの音量が下がります）。

## [リソース](/jp/design/human-interface-guidelines/multitasking#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/multitasking#Related)

[レイアウト](/jp/design/human-interface-guidelines/layout)

[ウインドウ](/jp/design/human-interface-guidelines/windows)

[ビデオの再生](/jp/design/human-interface-guidelines/playing-video)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/multitasking#Developer-documentation)

[アプリのローンチに対応する](/documentation/UIKit/responding-to-the-launch-of-your-app) — UIKit

[iPad、Mac、Apple Vision Proでのマルチタスク](/documentation/UIKit/multitasking-on-ipad-mac-and-apple-vision-pro) — UIKit

#### [ビデオ](/jp/design/human-interface-guidelines/multitasking#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/208)

[](https://developer.apple.com/videos/play/wwdc2025/282)

## [変更履歴](/jp/design/human-interface-guidelines/multitasking#Change-log)

日付| 変更内容  
---|---  
2025年6月09日| プラットフォームの考慮事項のガイダンスを再編成、およびiPadOSで複数のウインドウを使用したマルチタスクに関するガイダンスを追加。  
2023年12月05日| iPadOSのプライマリウインドウと補助ウインドウのアートワークを追加。  
2023年6月21日| visionOSのガイダンスを追加するために更新。
