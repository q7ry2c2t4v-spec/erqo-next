# プライバシー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/privacy

# プライバシー

プライバシーは最重要事項です。プライバシーに関連してデータやリソースが必要になる場合、透明性を確保することは非常に大切で、ユーザがアクセスを許可したデータを保護することも不可欠です。

![手のひらのスケッチ。保護を示しています。画像の上に長方形と円形のグリッド線が重ねられており、画像全体が6色の初代Appleロゴの黄色を連想させる黄色みを帯びています。](https://docs-assets.developer.apple.com/published/161fec1d77c705ccf076fb4c67d32f5c/foundations-privacy-intro%402x.png)

デバイスをどのように使用するかはユーザのきわめて個人的な事柄で、プライバシーの保護がアプリに期待されるのは当然です。

新規またはアプリのアップデートを提出する際、App Storeのプロダクトページに記載できるように、プライバシー方針および収集されるプライバシー関連データの詳細も提供してください。（この情報は[App Store Connect](https://help.apple.com/app-store-connect/#/dev1b4647c5b)でいつでも変更できます。）プロダクトページに詳しいプライバシー情報があれば、ユーザは十分な情報を得てから、アプリをダウンロードするかどうか決定できます。詳しくは、[App Storeのアプリのプライバシーの詳細](https://developer.apple.com/app-store/app-privacy-details/)を参照してください。

![App Storeのアプリのプロダクトページにある「アプリのプライバシー」画面。画面上方の「ユーザのトラッキングに使用されるデータ」に連絡先情報、その他のデータ、IDが表示されています。画面下方の「ユーザに関連付けられたデータ」には、ヘルスケアとフィットネス、財務情報、連絡先情報、購入、位置情報、連絡先が表示されています。](https://docs-assets.developer.apple.com/published/7addc07732d4d838762996845667ab53/privacy-social-media-app-store-nutrition-labels%402x.png)

App Storeのアプリのプロダクトページを見れば、ユーザはアプリをダウンロードする前にプライバシー方針を的確に把握できます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/privacy#Best-practices)

**実際に必要なデータ以外はアクセスをリクエストしない。** 機能で必要になる以上のデータを要求したり、ユーザがまだその機能に関心を示していないのにデータを要求したりすると、アプリを信頼してもらうのが難しくなることがあります。ユーザが自分のデータを緻密に管理できるように、アクセスのリクエストをできる限り具体的にしてください。

**アプリでのデータの収集方法と利用方法について透明性を確保する。** 収集した情報をアプリがどのように利用するのかが正確に分からなければ、ユーザは自分の情報をアプリと進んで共有しようという気持ちになれません。ユーザが、「メールを非公開」や「メールプライバシー保護」などのシステム機能を使用する場合はその選択を常に尊重し、アプリのトラッキングに関するアプリ側の義務を必ず理解してください。Appleのプライバシー機能について詳しくは、[プライバシー](https://www.apple.com/privacy/)を参照してください。デベロッパ向けのガイダンスは、[ユーザのプライバシーとデータの使用](https://developer.apple.com/app-store/user-privacy-and-data-use/)を参照してください。

**データはできる限りデバイス上で処理する。** 例えばiOSでは、Apple Neural EngineとカスタムのCreateMLモデルを利用して、データをデバイス上で直接処理できます。これは、リモートサーバとのやり取りに伴う長い時間と潜在的なリスクを回避する効果的な方法です。

**システムで定義されたプライバシー保護を採用し、セキュリティのベストプラクティスに従う。** 例えばiOS 15以降では、CloudKitを活用して、文字列、数値、日付などさまざまな種類のデータの暗号化および鍵管理を実現できます。

## [許可のリクエスト](/jp/design/human-interface-guidelines/privacy#Requesting-permission)

アクセス許可をリクエストする必要のある情報の例を以下に示します:

  * 位置情報、ヘルスケア、財務、連絡先情報、その他の個人を特定できる情報を含む個人データ

  * メール、メッセージ、カレンダーデータ、連絡先、ゲームプレイの情報、Apple Musicのアクティビティ、HomeKitデータ、オーディオ/ビデオ/写真のコンテンツなど、ユーザが生成したコンテンツ

  * Bluetoothデバイス、ホームオートメーション機能、Wi-Fi接続、ローカルネットワークなどの保護されたリソース

  * カメラやマイクなどのデバイスの機能

  * ハンドトラッキング、平面推定、画像アンカリング、ワールドトラッキングなど、フルスペースで実行されているvisionOSアプリのARKitデータ

  * アプリによるトラッキングに対応する、デバイスの広告識別子

システムには、アプリからのリクエストがあるたびにユーザにそれを通知する標準アラート機能があります。アプリがアクセスを必要とする理由を説明したテキストを提供すると、それがアラートに表示されます。ユーザは「設定」＞「プライバシー」でもこの説明を確認できます。設定を変更することもできます。

**明らかに当該データやリソースにアクセスする必要がある場合にのみ許可をリクエストする。** 個人情報やデバイスの機能の利用が要求されると、ユーザは不安になります。特にその必要があるかどうかはっきりしない場合はそうなるのも当然です。データアクセスを必要とするアプリ機能をユーザが実際に使用するまでは、許可をリクエストしないのが最善です。例えば、位置情報を必要とする機能をユーザが利用しようとした時点で初めて[位置情報ボタン](/jp/design/human-interface-guidelines/privacy#Location-button)を表示して、ユーザが自分の位置情報を共有する機能を提供できます。

**アプリを動作させるためにデータやリソースが必要でない限りアプリ起動時に許可をリクエストしない。** 起動時に許可が要求される理由がはっきりしていれば、それをユーザが煩わしく感じる可能性は低くなるでしょう。例えば、ナビゲーションアプリを実際に利用するには、その前にユーザの位置情報が必要になることは理解してもらえるはずです。同様に、周囲の壁に仮想オブジェクトを当てて跳ね返らせるvisionOSゲームをプレイするには、周囲に関する情報へのアクセスをユーザからゲームに対して許可する必要があります。

**アプリがリクエストしている機能、データ、リソースがアプリでどのように使用されるのかを明確に記述しておく。** 標準アラートでは、アプリ名と、ユーザがリクエストを許可/拒否するボタンの間に、指定された文言が表示されます（これを _目的文字列_ または _使用方法の説明文_ といいます）。簡潔、かつ単刀直入で具体的な分かりやすい文章を指定してください。受動態を避け、文末に句点を付けるようにしてください。デベロッパ向けのガイダンスは、[保護されたリソースへのアクセスをリクエストする](/documentation/UIKit/requesting-access-to-protected-resources)および[App Tracking Transparency](/documentation/AppTrackingTransparency)を参照してください。

| 目的文字列の例| メモ  
---|---|---  
![丸に囲まれたチェックマークが適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| このアプリはいびきの音を検出する目的で夜間にデータを録音します。| アプリがデータを収集する方法と理由を明確に説明する能動態の文。  
![丸に囲まれたX印が不適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)| 体験向上のためにはマイクの利用が必要とされます。| あいまいで不明瞭な理由が記された受動態の文。  
![丸に囲まれたX印が不適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)| マイクをオンにしてください。| 何の理由も示していない命令形の文。  
  
標準のシステムアラートの例を以下に示します:

![Social Mediaアプリの許可アラート。「”Social Media”に位置情報の使用を許可しますか?  位置情報をオンにすると、近くの場所の投稿を表示できます。」という目的文字列が表示されています。文字列の下の小さい地図画像に「正確な位置情報: オン」と表示され、地図の下にボタンが3つあります。上から「1度だけ許可」、「アプリの使用中は許可」、「許可しない」です。](https://docs-assets.developer.apple.com/published/ac1e97ee6c2655fc4453bf9c7be692f3/privacy-social-media-post-location-alert%402x.png)

![Social Mediaアプリの許可アラート。「”Social Media”から“写真”にアクセスしようとしています。ライブラリにある写真のアップロードを許可してください。」という目的文字列が表示されています。文字列の下にボタンが3つあります。上から「写真を選択…」、「すべての写真へのアクセスを許可」、「許可しない」です。](https://docs-assets.developer.apple.com/published/cb6b1dc22a6244278d2535876bb42c8b/privacy-social-media-post-photo-alert%402x.png)

![Social Mediaアプリの許可アラート。「”Social Media”が連絡先へのアクセスを求めています。Social Mediaで友達を見つけてネットワークに参加しましょう。」という目的文字列が表示されています。文字列の下に2つのボタンが並んで表示されています。「許可しない」と「許可」です。](https://docs-assets.developer.apple.com/published/d1fec324515f199cd0274da4953a8cf8/privacy-social-media-friends-contacts-alert%402x.png)

### [プレアラート画面、ウインドウ、ビュー](/jp/design/human-interface-guidelines/privacy#Pre-alert-screens-windows-or-views)

なぜアプリが許可をリクエストしているのか、ユーザが現在の状況からすぐに理解できるなら理想的ですが、どうしても詳細な情報を提供してもらう必要がある場合は、システムアラートが表示される前にカスタム画面またはウインドウを表示できます。カメラ、マイク、位置情報、連絡先、カレンダー、トラッキング情報など、保護対象のデータやリソースへのアクセス許可をリクエストするシステムアラートよりも前に表示されるカスタムビューには、以下のガイドラインが適用されます。

**表示するボタンは1つだけにし、タップすると次にシステムアラートが表示されることがはっきり分かるようにする。** タップしてもアラートが開かないボタンがカスタムの画面やウインドウに含まれていると、選択から意識がそれてしまうので、ユーザが都合よく操られているように感じてしまうかもしれません。カスタム画面のボタンを「許可」のようなタイトルにするのも、そのような操作に該当します。カスタム画面のボタンが意味や視覚的な重みの点でアラートの許可ボタンに似ていると、そうするつもりがないのにアラートの許可ボタンを選択してしまう可能性が高まるからです。カスタムの画面やウインドウに、「続ける」とか「次へ」のようなタイトルのボタンを1つだけ配置すれば、次にシステムアラートが表示されるとはっきり分かります。

![アプリのプレアラート画面。「位置情報サービスをオンにすると、以下の機能が提供されます: 友達が近くにいるときに通知、近くで開催中のイベントのニュース、自分の位置情報のタグ付けと共有。これはあとで設定アプリで変更できます。」と表示されています。テキストの下のボタンは「次へ」というタイトルになっています。](https://docs-assets.developer.apple.com/published/8a4129798f8d4c039c84ee9390a99341/privacy-custom-messaging-correct%402x.png)

![丸に囲まれたチェックマークが適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

**カスタムの画面やウインドウに追加のアクションを含めない。** 例えば、「閉じる」や「キャンセル」などのボタンを用意することで、システムアラートが表示される前に画面やウインドウを閉じられるようにはしないでください。

![アプリのプレアラート画面。「次へ」ボタンの下に表示されている「キャンセル」というボタンが含まれています。](https://docs-assets.developer.apple.com/published/826ffb70f28082f56fda0cec1561bcd8/privacy-custom-messaging-incorrect-cancel-button%402x.png)

![丸に囲まれたX印が不適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)キャンセルするオプションは含めないでください。

![アプリのプレアラート画面。左上隅に「閉じる」ボタンが含まれています。画面の下の方に「次へ」ボタンが表示されています。](https://docs-assets.developer.apple.com/published/948765125cb23f14d9b1f7daf875c3fe/privacy-custom-messaging-incorrect-close-button%402x.png)

![丸に囲まれたX印が不適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)ビューを閉じるオプションは含めないでください。

### [トラッキングのリクエスト](/jp/design/human-interface-guidelines/privacy#Tracking-requests)

アプリのトラッキングはデリケートな問題です。トラッキングのメリットを説明するカスタムの画面やウインドウを表示するのがよいと考えられる状況もあります。ユーザがアプリを起動した直後からアプリのトラッキングを実行したい場合は、トラッキングデータを収集する前に、システムが提供しているアラートを表示する必要があります。

**システムが提供するアラートよりも前に、ユーザが混乱したり誤解したりしかねないカスタムの画面やウインドウを表示しない。** アラートをよく読まずにすぐに閉じてしまうユーザもいます。そのような行動を利用してユーザの選択に影響を与えようとするカスタムのメッセージ画面、ウインドウ、ビューは、App Storeの審査で公開拒否される原因になります。

公開拒否の原因となる、カスタム画面で禁止されているデザインはいくつかあります。例えば、インセンティブを申し出る、リクエストのように見せかける画面やウインドウを表示する、アラートの画像を含める、アラートに注釈を付けるなどです（下の例を参照）。詳細は、[App Reviewガイドライン5.1.1 (iv)](https://developer.apple.com/app-store/review/guidelines/#data-collection-and-storage)を参照してください。

![アプリのプレトラッキングメッセージ。「トラッキングを許可して、次回の購入に使える100ドルのクレジットをもらおう。」と表示されています。このテキストの下に円で囲まれたドル記号の画像があります。画像の下のボタンは「100ドルのクレジットをもらう」となっています。](https://docs-assets.developer.apple.com/published/c335f0c3e8ef59cbaee84251590d6ddd/privacy-custom-messaging-prohibited-incentive%402x.png)

![丸に囲まれたX印が不適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)要求の許可を得ようとしてインセンティブを提供してはなりません。権限付与に対する報酬をユーザに提供することはできません。ユーザがトラッキングを許可するまで機能やコンテンツの提供を停止したり、アプリを利用できなくしたりすることもできません。

![アプリのプレトラッキングメッセージ。「トラッキングを許可すると体験が向上します。」と表示されています。テキストの下にある棒グラフの画像には、左から右へと高さが増していく4つの棒があります。グラフの下のボタンは「トラッキングを許可」となっています。](https://docs-assets.developer.apple.com/published/01ca9d9824477c4917b3e3a0439fb20f/privacy-custom-messaging-prohibited-imitation%402x.png)

![丸に囲まれたX印が不適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)システムアラートの機能とそっくりなカスタム画面を表示してはなりません。特に、「許可」やそれと同義の語を含むボタンタイトルを作成しないでください。プレアラート画面ではユーザは何も許可できません。

![アプリのプレトラッキングメッセージ。「メッセージが表示されたら「許可」を選んでください。」と表示されています。このテキストの下には、システムが提供するアラートの画像があります。画像の下のボタンは「続ける」というタイトルになっています。システム標準のアラートの画像の「アプリの使用中は許可」ボタンは丸で囲まれています。](https://docs-assets.developer.apple.com/published/fa998ea875ec0f7751b76435b1958cae/privacy-custom-messaging-prohibited-alert%402x.png)

![丸に囲まれたX印が不適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)加工した標準アラートの画像を表示してはなりません。

![アプリのプレトラッキングメッセージ。「トラッキングを許可すると体験が向上します。」と表示されています。アプリのカスタム画面の下3分の1の位置に、上向きの矢印と「「許可」を選択」という文言があります。](https://docs-assets.developer.apple.com/published/c3f363af1a30b40a2d185c824425e3da/privacy-custom-messaging-prohibited-alert-annotation%402x.png)

![丸に囲まれたX印が不適切な例であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)ユーザの注意をシステムアラートの「許可」ボタンに向けるような視覚的刺激を追加してはなりません。

## [位置情報ボタン](/jp/design/human-interface-guidelines/privacy#Location-button)

iOS、iPadOS、watchOSのCore Locationでは、特定のタスクが位置情報を必要とする時点で一時的なアクセス権限をアプリに付与するボタンをユーザに表示できます。位置情報ボタンの見た目はアプリのUIに合わせて調整できます。位置情報ボタンは、位置情報を共有する操作と常に連動しており、ユーザは瞬時にその意味を理解できます。

![角丸四角形の青いボタンと白い位置情報インジケータ（右上を指す矢印に続けて「現在地」と表示されている）の画像。](https://docs-assets.developer.apple.com/published/790bf8f90d69a4a8709f9d0993a6c477/location-button%402x.png)

ユーザがアプリを開いて最初に位置情報ボタンをタップすると、システムの標準アラートが表示されます。アラートには、ユーザがこのボタンでアプリによる位置情報の利用を制限できることが示され、位置情報の共有が開始されると位置情報インジケータがどのように表示されるかも分かります。

![背景画像に重ねて表示される位置情報ボタンのアラート。一部が地図に表示されています。「ソーシャルメディアに位置情報の利用を許可しますか? 位置情報サービスをオンにすると、近くのポストの位置情報を表示できます。」というアラートが表示されています。このテキストの下に小さい地図の画像があり、クパティーノ周辺が拡大されています。地図の下にボタンが3つあり、上から「1度だけ許可」、「アプリの使用中は許可」、「許可しない」です。](https://docs-assets.developer.apple.com/published/b04d69db90690dd45e1fe58ad271fe2d/privacy-social-media-map-location-alert%402x.png)

ユーザはボタンの意味を理解したら、位置情報ボタンをタップするだけで自分の位置情報を利用する1回限りの権限をアプリに付与することができます。1回限りの権限はユーザがアプリの使用を停止すると期限切れになりますが、次回からボタンの動作について確認する必要はなくなります。

備考

認可のないアプリの場合、位置情報ボタンのタップは、標準アラートで「 _1度だけ許可_ 」を選択した場合と同じ動作になります。ユーザが以前に「 _このアプリの使用中のみ許可_ 」を選択している場合は、位置情報ボタンをタップしてもアプリの認可ステータスは変わりません。デベロッパ向けのガイダンスは、[`LocationButton`](/documentation/CoreLocationUI/LocationButton)（SwiftUI）および[`CLLocationButton`](/documentation/CoreLocationUI/CLLocationButton)（Swift）を参照してください。

**特定のアプリ機能のためにユーザの位置情報を共有する手軽な方法として位置情報ボタンを活用する。** 例えば、気軽にメッセージや投稿に自分の位置情報を添付したり、お店を見つけたり、今いる場所で見かけた建物や植物、動物について尋ねたりできるアプリを開発できます。多くのユーザがアプリで「 _1度だけ許可_ 」をタップすると分かっているなら、アラートに繰り返し応答しなくても位置情報を簡単に共有できる位置情報ボタンの利用を検討してください。

**アプリのUIに最適な位置情報ボタンのカスタマイズを検討する。** 具体的には以下のカスタマイズが可能です:

  * システムが提供するタイトルのなかから、「現在地」や「自分の現在地を共有」など機能を最もよく表すものを選びます。

  * 位置を示すグリフは、塗りつぶしまたはアウトラインを選びます。

  * 背景、タイトル、グリフの色を選択します。

  * ボタンの角の丸みを調整します。

視認性と信頼性の高い位置情報ボタンにするため、ボタンのその他の視覚属性はカスタマイズできません。さらに、位置情報ボタンの高い視認性を保証するため、コントラストが低い色の組み合わせや過度の半透明度などの問題がある場合には、システムから警告が出力されます。このような問題の修正に加えて、テキストがボタン内に収まるようにする必要もあります。例えば、アクセシビリティテキストサイズを変更したり他言語に翻訳したりしてもテキストの切り捨てが発生しないようにしてください。

重要

カスタマイズ後の位置情報ボタンの問題が解決していないとシステムが認識した場合、ユーザが位置情報ボタンをタップしてもアプリからデバイスの位置情報にアクセスできなくなります。このようなボタンであっても、アプリに固有のその他のアクションを実行することはできますが、位置情報ボタンが期待通りに動作しなければ、アプリに対するユーザの信頼が損なわれる可能性があります。

## [データの保護](/jp/design/human-interface-guidelines/privacy#Protecting-data)

ユーザ情報の保護は最も重要です。情報をローカルに保存したり、ユーザの特定の操作を承認したり、情報をネットワークで送ったりする必要がある場合に、システムが提供するセキュリティテクノロジーを利用すれば、アプリのセキュリティを信頼してもらえるようになり、ユーザのプライバシーの保護に貢献できます。

全体的なガイドラインは以下の通りです。

**パスワードに加えてほかの認証方法を設ける。** なるべく、パスワードの代わりに[パスキー](https://developer.apple.com/documentation/authenticationservices/public-private_key_authentication/supporting_passkeys/)を使ってください。認証にパスワードの使用を続ける必要がある場合でも、2ファクタ認証によってセキュリティを強化してください（デベロッパ向けのガイダンスは、[iCloudキーチェーン認証コードでログインのセキュリティを確保する](/documentation/AuthenticationServices/securing-logins-with-icloud-keychain-verification-codes)を参照してください）。ユーザがデバイスで常時ログインしているアプリへのアクセスをさらに保護するには、Face ID、Optic ID、Touch IDなどの生体認証を使用します。デベロッパ向けのガイダンスは、[Local Authentication](/documentation/LocalAuthentication)を参照してください。

**機密情報をキーチェーンに保存する。** キーチェーンは安全性が高く、ユーザは安心してスムーズに個人情報を操作できます。デベロッパ向けのガイダンスは、[キーチェーンサービス](/documentation/Security/keychain-services)を参照してください。

**パスワードその他のセキュリティコンテンツを標準テキストで保存しない。** ファイルのアクセス権を使ってアクセスを制限しているとしても、機密情報は暗号化されたキーチェーンに保存する方がはるかに安全です。

**カスタムの認証方式を考案して使わない。** 認証が必要なアプリでは、[パスキー](https://developer.apple.com/documentation/authenticationservices/public-private_key_authentication/supporting_passkeys/)、[Appleでサインイン](/jp/design/human-interface-guidelines/sign-in-with-apple)、[パスワード自動入力](/documentation/Security/password-autofill)など、システムが提供する機能を優先して使用してください。関連するガイダンスは、[アカウントの管理](/jp/design/human-interface-guidelines/managing-accounts)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/privacy#Platform-considerations)

 _iOS、iPadOS、tvOS、watchOSに追加の考慮事項はありません。_

### [macOS](/jp/design/human-interface-guidelines/privacy#macOS)

**有効なデベロッパIDでアプリに署名する。** アプリをApp Store外で配布する場合、デベロッパIDでアプリに署名しておけば、署名者がAppleデベロッパであり、安全に使用できるアプリであると認識されます。デベロッパ向けのガイダンスは、[Xcodeヘルプ](https://developer.apple.com/go/?id=ios-app-distribution-guide)を参照してください。

**アプリをサンドボックス化してユーザのデータを保護する。** サンドボックス化すると、アプリにシステムリソースやユーザデータのアクセス権を付与すると同時に、情報をマルウェアから保護できます。Mac App Storeに提出するアプリはすべてサンドボックス化する必要があります。デベロッパ向けのガイダンスは、[macOSアプリのサンドボックスの構成](/documentation/Xcode/configuring-the-macos-app-sandbox)を参照してください。

**どんなユーザがサインインしているかを決めてかからない。** ファストユーザスイッチを利用して、複数のユーザが同じシステムを使用している可能性があります。

### [visionOS](/jp/design/human-interface-guidelines/privacy#visionOS)

visionOSではデフォルトでARKitアルゴリズムを使って、パーシステンス、ワールドマッピング、セグメンテーション、マッティング、環境照明などの機能を実行します。これらのアルゴリズムは常時動作しているので、共有スペースで実行しているアプリやゲームは、ARKitを自動的に利用することができます。

ARKitから共有スペースのアプリにデータが送信されることはありません。ARKit APIを利用するには、アプリでフルスペースを開く必要があります。加えて、平面推定、シーン再構築、画像アンカリング、ハンドトラッキングなどの機能では、いかなる情報にアクセスする場合にもユーザの許可が必要です。デベロッパ向けのガイダンスは、[ARKitデータのアクセスを設定する](/documentation/visionOS/setting-up-access-to-arkit-data)を参照してください。

visionOSは、ユーザ入力のプライバシーを保護する設計になっています。SwiftUIまたはRealityKitを使用して作成されたインタラクティブコンポーネントをユーザが注視したときは、自動的に表示されるホバーエフェクトによってユーザに視覚フィードバックが返され、タップ前にユーザが見ていた位置がアプリに渡されることはありません。ガイダンスは、[視線](/jp/design/human-interface-guidelines/eyes)および[ジェスチャ＞visionOS](/jp/design/human-interface-guidelines/gestures#visionOS)を参照してください。

visionOSでは、デバイスカメラへのデベロッパアクセスがほかのプラットフォームと異なります。具体的には、バックカメラは空の入力を返すため、互換性を確保する目的にしか使えません。フロントカメラは[空間Persona](/jp/design/human-interface-guidelines/shareplay#visionOS)用の入力を返しますが、この入力を利用できるのはユーザが許可した場合に限ります。visionOSに移植しようとしているiOSまたはiPadOSのアプリに、カメラへのアクセスが必要な機能が含まれている場合は、その機能を削除するか、代わりにユーザがコンテンツを読み込むオプションに置き換えてください。デベロッパ向けのガイダンスは、[既存のアプリをvisionOSに対応させる](/documentation/visionOS/making-your-app-compatible-with-visionos)を参照してください。

## [リソース](/jp/design/human-interface-guidelines/privacy#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/privacy#Related)

[データの入力](/jp/design/human-interface-guidelines/entering-data)

[オンボーディング](/jp/design/human-interface-guidelines/onboarding)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/privacy#Developer-documentation)

[保護されたリソースへのアクセスをリクエストする](/documentation/UIKit/requesting-access-to-protected-resources) — UIKit

[Security](/documentation/Security)

[位置情報サービスを使用する権限をリクエストする](/documentation/CoreLocation/requesting-authorization-to-use-location-services) — CoreLocation

[App Tracking Transparency](/documentation/AppTrackingTransparency)

#### [ビデオ](/jp/design/human-interface-guidelines/privacy#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/246)

[](https://developer.apple.com/videos/play/wwdc2025/279)

[](https://developer.apple.com/videos/play/wwdc2024/10123)

## [変更履歴](/jp/design/human-interface-guidelines/privacy#Change-log)

日付| 変更内容  
---|---  
2023年6月21日| ガイダンスを新規ページに統合し、visionOSに対応するように更新。
