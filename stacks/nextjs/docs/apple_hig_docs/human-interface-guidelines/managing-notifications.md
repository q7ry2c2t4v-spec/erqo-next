# 通知の管理

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/managing-notifications

# 通知の管理

通知を利用すると、デバイスがロック中でも使用中でも、重要な情報をタイムリーに届けることができます。

![ベルに小さい丸が重なっているスケッチ。通知音を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせるオレンジ色になっています。](https://docs-assets.developer.apple.com/published/47ea47dcc62c34376954423cc3fe1ab5/patterns-managing-notifications-intro%402x.png)

通知を送るには、あらかじめ許可を得る必要があります。ユーザは、設定から通知の許可を変更したり、すべての通知をオフにしたりすることができます（一部の地域での政府からの通知は除きます）。

## [集中モードへの対応](/jp/design/human-interface-guidelines/managing-notifications#Integrating-with-Focus)

自分にとって重要な通知を受け取れることはありがたいことですが、通知に邪魔されたくないと思うときもあります。そのような場合に対応できるように、通知の配信時間を指定したり、集中モードを設定したりできるようになっています。

  * 集中モードを使うと、睡眠、仕事、読書、運転などに集中している間、通知をフィルタリングすることができます。

  * 配信スケジュールを設定すると、すぐに通知を受け取るか、指定した時間に通知の要約を受け取るかを選択できます。

ユーザは、集中モードがオンのときに通知を表示する連絡先やアプリを指定できます。例えば、「仕事」集中モードでは、同僚や家族、仕事関連のアプリからの通知をすぐに表示することができます。集中モードをオンにしているときでも、即時通知はすべて表示するようにすることもできます。 _即時通知_ とは、すぐに届けられた方がよい重要な情報を含む通知です。

重要

集中モードでは通知が届いてもすぐに表示されないことがありますが、通知自体は届いた瞬間から利用できます。

この動作をカスタマイズできるようにするため、まずアプリやゲームで送信する通知の種類を決めてください。通話やメッセージなどの直接的なコミュニケーションに対応する場合は _コミュニケーション_ 通知を、それ以外のタスクには _ノンコミュニケーション_ 通知を使います。コミュニケーション通知に対応するには、SiriKitのIntentを使います。つまり、ユーザがSiriを使って通知の動作をカスタマイズできるようにします。デベロッパ向けのガイダンスは、[`INSendMessageIntent`](/documentation/Intents/INSendMessageIntent)および[`UNNotificationContentProviding`](/documentation/UserNotifications/UNNotificationContentProviding)を参照してください。

ノンコミュニケーション通知では、送信する通知ごとにシステムで定義されている中断レベルを指定する必要があります。通知が表示されるタイミングは、中断レベルに応じて決まります。コミュニケーション通知が届いた際に通知が表示されるタイミングは送信者に応じて決まります。

ノンコミュニケーション通知では、4つの中断レベルが定義されています:

  * _passive_ : ユーザが好きなタイミングで通知を表示します。レストランのおすすめなどがこれに当たります。

  *  _active_ （デフォルト）: 着信したタイミングで知ることができるとありがたい情報です。お気に入りのスポーツチームの得点に関する最新情報などがこれに当たります。

  *  _timeSensitive_ （即時通知）: ユーザに直接的に影響し、すぐに対応する必要がある情報です。アカウントのセキュリティ問題や荷物の配達などがこれに当たります。

  *  _critical_ : ユーザに直接的に影響し、すぐに対応する必要がある情報のうち、健康や安全に関する緊急情報です。criticalレベルの通知は非常にまれで、通常は政府や公的機関、または健康や自宅を管理するアプリから発信されます。

システムで定義された中断レベルの通知は、次のように動作します。

中断レベル| スケジュールに関係なく配信| 集中モード中に通知| iPhoneやiPadの着信/サイレントスイッチを無視  
---|---|---|---  
passive| しない| しない| しない  
active| しない| しない| しない  
timeSensitive| する| する| しない  
critical| する| する| する  
  
注意

criticalレベルの通知は着信/サイレントスイッチを無視でき、スケジュールや集中モードに関係なく配信されるため、エンタイトルメントがないと送信できません。

## [ベストプラクティス](/jp/design/human-interface-guidelines/managing-notifications#Best-practices)

**それぞれの通知内容を適切に反映した緊急度を設定することで信頼を得るようにする。** ユーザは、いくつかの方法で通知の受け取りかたを調整できます。これにはすべての通知をオフにすることも含まれるので、できる限り実情に即した中断レベルを割り当てることが重要です。高い緊急度を使って優先度の低い情報を通知し、ユーザの作業を邪魔していると思われないようにしましょう。

**timeSensitive（即時通知）中断レベルは、すぐに通知しなければならないことだけに使用する。** 集中モードやスケジュール配信を無視してでも通知するメリットを理解してもらうため、即時通知は、今起きていることや1時間以内に起きることについての通知にのみ限定してください。アプリから初めて即時通知が着信すると、この通知の仕組みの説明が表示され、その情報にすぐに注目する必要はないと思う場合に通知をオフにする方法が示されます。その後も、即時通知の動作を評価する機会が定期的に与えられます。デベロッパ向けのガイダンスは、[`UNNotificationInterruptionLevel`](/documentation/UserNotifications/UNNotificationInterruptionLevel)を参照してください。

## [マーケティング通知の送信](/jp/design/human-interface-guidelines/managing-notifications#Sending-marketing-notifications)

マーケティングや宣伝のコンテンツは、ユーザが明示的に受け取りに同意した場合を除き、通知を使って送信しないようにしてください。アプリやゲームの新しい機能、コンテンツ、イベントについて知りたい場合に、ユーザがマーケティングの通知を送信する許可を与えることができます。例えば、サブスクリプションアプリを使っているユーザなら、サブスクリプションに登録するオファーを受け取りたいかもしれません。また、ゲームのプレイヤーなら、ゲームのライブイベントに関連する特別なオファーを受け取りたいかもしれません。

**マーケティングの通知はtimeSensitive中断レベルでは送らないようにする。** ユーザがアプリからマーケティングの通知を受け取ることに同意した場合でも、そのような通知で集中モードやスケジュール配信設定を無視してはいけません。

**宣伝やマーケティングの通知を送りたい場合はユーザの許可を得るようにする。** このような通知を送信する前には、ユーザから明示的に許可を得る必要があります。警告やモーダルビューなどのインターフェイスを作成して送りたい情報の種類を説明し、ユーザが分かりやすい方法で有効にするか無効にするかを選択できるようにしましょう。

**ユーザがアプリで通知設定を管理できるようにする。** 情報やマーケティングの通知を送る許可を求めるだけでなく、ユーザがその選択を変更できるアプリ内設定画面も提供する必要があります。ガイダンスは、[設定](/jp/design/human-interface-guidelines/settings)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/managing-notifications#Platform-considerations)

 _iOS、iPadOS、macOS、tvOS、visionOSに追加の考慮事項はありません。_

### [watchOS](/jp/design/human-interface-guidelines/managing-notifications#watchOS)

デフォルトで、Apple Watchのアプリの通知設定には、iPhoneの同じアプリの設定が適用されます。ユーザは、iPhoneのApple Watchアプリで設定を管理できます。また、Apple Watchに通知が着信したときに左にスワイプして、「1時間通知を停止」や「即時通知をオフにする」などの通知ごとのオプションにアクセスすることもできます。

## [リソース](/jp/design/human-interface-guidelines/managing-notifications#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/managing-notifications#Related)

[プライバシー](/jp/design/human-interface-guidelines/privacy)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/managing-notifications#Developer-documentation)

[User Notifications](/documentation/UserNotifications)

#### [ビデオ](/jp/design/human-interface-guidelines/managing-notifications#Videos)

[](https://developer.apple.com/videos/play/wwdc2021/10091)

[](https://developer.apple.com/videos/play/wwdc2020/10095)
