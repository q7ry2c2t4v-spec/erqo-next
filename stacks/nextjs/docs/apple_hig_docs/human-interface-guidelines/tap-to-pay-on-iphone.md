# iPhoneのタッチ決済

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/tap-to-pay-on-iphone

# iPhoneのタッチ決済

「iPhoneのタッチ決済」は、外部端末を接続することなくiPhone上のアプリを使って非接触型の支払いを受領することができる店舗向け機能です。

![円の中に右に向かって徐々に大きくなる曲線のスケッチ。「iPhoneのタッチ決済」を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる青色になっています。](https://docs-assets.developer.apple.com/published/6c0a28561096373fdfde750efa10bac1/technologies-TapToPay-intro%402x.png)

iOS支払いアプリで「iPhoneのタッチ決済」に対応する場合は、店舗側から顧客に対して一貫性があり信頼のおける操作を提示できるようにしましょう。

備考

「iPhoneのタッチ決済」は、既存の支払い受領端末やアクセサリと併用できます。

「iPhoneのタッチ決済」をiOSアプリに組み込む前に、決済サービスプロバイダ（PSP）と連携して、「iPhoneのタッチ決済」エンタイトルメントをリクエストし、PSPのSDKを通じて、またはフレームワークを導入して、[ProximityReader](/documentation/ProximityReader) APIを使用する必要があります。アプリの新機能について周知する際のマーケティング推奨事項を含むガイダンスの概要は、[iPhoneのタッチ決済](https://developer.apple.com/tap-to-pay/)を参照してください。デベロッパ向けのガイダンスは[「iPhoneのタッチ決済」を設定する](/documentation/ProximityReader/setting-up-the-entitlement-for-tap-to-pay-on-iPhone)を参照してください。

注意

PSPから、タップ結果を表示するなどの操作を含むユーザインターフェイスが組み込まれたSDKが提供されている場合は、PSPが提供するドキュメントを参照してください。

## [「iPhoneのタッチ決済」の有効化](/jp/design/human-interface-guidelines/tap-to-pay-on-iphone#Enabling-Tap-to-Pay-on-iPhone)

アプリで「iPhoneのタッチ決済」を有効にして店舗のデバイスを構成する前に、関連する利用規約に同意する必要があります。ProximityReader APIを使用して現在のステータスを取得して、必要な場合のみ同意フローを表示するようにします。デベロッパ向けのガイダンスは、[アプリで「iPhoneのタッチ決済」に対応する](/documentation/ProximityReader/adding-support-for-tap-to-pay-on-iphone-to-your-app#Display-the-Terms-and-Conditions-interface-to-the-merchant)を参照してください。

**顧客応対を始める前に店舗が「iPhoneのタッチ決済」の利用規約に同意できるようにする。** 店舗側は初期デバイス構成の前に利用規約に同意する必要があるため、会計などの顧客応対フローを始める前に同意できるようになっていると便利です。例えば、[アプリ内メッセージ](https://developer.apple.com/tap-to-pay/marketing-guidelines/#in-your-app)やオンボーディングのフロー中に、「iPhoneのタッチ決済」の利用規約に同意するボタンを設けます。

![アプリ画面の図。機能の説明と、「iPhoneのタッチ決済を有効にする」というラベルが付いたボタンが表示されています。](https://docs-assets.developer.apple.com/published/2b61399beb78a2a4f208eaf1522d7fe1/tap-to-pay-introduction-screen%402x.png)「iPhoneのタッチ決済」の利用規約に同意する方法が提示されているアプリ画面

![アプリ画面の図。「テスト取引を試す」というラベルが付いたボタンが表示されています。](https://docs-assets.developer.apple.com/published/b9ef6c70fad5a8e3bd333b99c2f9ad1f/tap-to-pay-confirmation-screen%402x.png)「iPhoneのタッチ決済」が有効になっていて、それを試す方法が提示されているアプリ画面

**「iPhoneのタッチ決済」の利用規約は管理ユーザのみに表示する。** 非管理者が「iPhoneのタッチ決済」をアクティベートしようとした場合には、管理者アクセスが必要である旨のメッセージを表示します。アプリのプライマリユーザが企業や非管理者である場合は、管理者がWebインターフェイスや別のアプリ（iPhone以外のデバイスで動作するものも含む）から「iPhoneのタッチ決済」の利用規約に同意できるようにします。実装の詳細は、PSPにお問い合わせください。

**必要に応じて、デバイスが最新状態になっていることを店舗が確認できるようにする。** PSPが特定のバージョンのiOSを必要とする場合は、店舗でデバイスのアップデートが行われたあとにのみ、利用規約を表示します。

## [店舗への教育](/jp/design/human-interface-guidelines/tap-to-pay-on-iphone#Educating-merchants)

「iPhoneのタッチ決済」についてよく知らない店舗もあるかもしれません。そのため、素早く簡単に使い始めることができる方法を提示することが重要です。

**対応する決済タイプを説明したチュートリアルを提供し、「iPhoneのタッチ決済」でそれぞれのタイプに対処する方法を説明する。** このチュートリアルは、以下の方法で提示できます:

  * アプリ内メッセージの「詳細」オプションに含める

  * 店舗が「iPhoneのタッチ決済」の利用規約に同意した際に、自動的に表示する

  * アプリの新規ユーザに自動的に表示する

  * 簡単に探せるように、アプリのヘルプコンテンツや設定画面などの一貫した場所に入れる

[「iPhoneのタッチ決済」マーケティングガイドライン](https://developer.apple.com/tap-to-pay/marketing-guidelines/)のAppleが承認したアセットを使用してアプリのチュートリアルを作成できます。[`ProximityReaderDiscovery`](/documentation/ProximityReader/ProximityReaderDiscovery) APIを使用してあらかじめ作成した店舗教育を行うこともできます。Appleは、このAPIが最新で、店舗の地域向けにローカライズされていることを保証します。

![「設定」のアプリのチュートリアル画面の図。店舗教育チュートリアルを開くリンクがあります。](https://docs-assets.developer.apple.com/published/6e4f01e90092b71a1a173c0bdf4c9726/tap-to-pay-merchant-settings-tutorials%402x.png)

アプリの設定領域から、常にチュートリアルを利用できるようにしておくとよいでしょう。

![「iPhoneのタッチ決済」店舗教育チュートリアルシートの図。タッチ決済の動作の画像、最初の支払いを受領する方法の説明が含まれています。](https://docs-assets.developer.apple.com/published/e5bab425805217aa9d34d7107b751d75/tap-to-pay-merchant-education-contactless-cards%402x.png)

`ProximityReaderDiscovery` APIで提供される店舗教育チュートリアル。

専用のチュートリアルをデザインする場合は、以下の方法を示すようにしてください:

  * それぞれの支払いのタイプで会計フローを開始する

  * 顧客が非接触カードまたはデジタルウォレットを店舗の支払い用デバイスの適切な場所に置けるようにする

  * カードのPIN入力に対応する（アクセシビリティモードを含む）

また、「iPhoneのタッチ決済」の利用規約にまだ同意していない場合は、店舗向けチュートリアルの最後で同意できるようにします。

## [会計](/jp/design/human-interface-guidelines/tap-to-pay-on-iphone#Checking-out)

会計は、限られた時間の中で行う必要があるアクションです。そのため、店舗がスムーズに操作できるプロセスである必要があります。会計フローをデザインする際には、以下の点を念頭に置いてください:

  * 必要に応じて、「iPhoneのタッチ決済」以外の支払いオプションを提供する

  * 店舗が「iPhoneのタッチ決済」を有効にする前に会計を開始した場合、即座に対応する

  * デバイスが構成中の場合でも、店舗が会計を実行できるようにする

  * 最終合計金額に影響する支払い前アクションは、会計の完了前に提示する

**「iPhoneのタッチ決済」が有効化されているかどうかにかかわらず、会計オプションとして「iPhoneのタッチ決済」を提示する。** 「iPhoneのタッチ決済」ボタンを含めることで、店舗は会計フローを抜けることなく、柔軟にこの機能を利用できるようになります。店舗がこのボタンをタップしたときには、必要に応じて利用規約を提示し、構成完了後に、「iPhoneのタッチ決済」画面を自動的に表示します。

**「iPhoneのタッチ決済」が使えるようになるまでの待機時間を作らない。** 「iPhoneのタッチ決済」は、各デバイスの初期構成に加えて、アプリが最前面になるたびにも構成が必要です。ここで発生する可能性のある待機時間を最小限に抑えるには、アプリの起動後および最前面への移動直後に「iPhoneのタッチ決済」機能が利用できるよう準備します。デベロッパ向けのガイダンスは、[`prepare(using:)`](/documentation/ProximityReader/PaymentCardReader/prepare\(using:\))を参照してください。

**バックグラウンドで構成が進行中でも「iPhoneのタッチ決済」の会計オプションを選択できるようにする。** 店舗は会計時に毎回「iPhoneのタッチ決済」の会計オプションを選択する必要があります。構成の完了を待ってからオプションを選択可能にするのではなく、構成中でもこのオプションを選択できるようにし、選択後に進行状況インジケータを表示するようにしてください。ほとんどのシナリオで不確定的な進行状況インジケータを表示できますが、ProximityReader APIで構成が進行中であると表示された場合は、確定的な進行状況インジケータを表示します。ガイダンスは[進行状況インジケータ](/jp/design/human-interface-guidelines/progress-indicators)を参照してください。デベロッパ向けのガイダンスは[`PaymentCardReader.Event.updateProgress(_:)`](/documentation/ProximityReader/PaymentCardReader/Event/updateProgress\(_:\))を参照してください。

![アプリ画面の図。合計購入額の上に、確定的な進行状況インジケータと「iPhoneのタッチ決済を準備中」というテキストが表示されています。](https://docs-assets.developer.apple.com/published/2297c73c770d15521479897d929256cb/tap-to-pay-processing-screen-determinate-progress%402x.png)構成中に確定的な進行状況インジケータが表示されているアプリ画面

![アプリ画面の図。合計購入額の上に、不確定的な進行状況インジケータと「iPhoneのタッチ決済を準備中」というテキストが表示されています。](https://docs-assets.developer.apple.com/published/aa890391fa9437a3f337e7f98737a5ee/tap-to-pay-processing-screen-indeterminate-progress%402x.png)構成中に不確定的な進行状況インジケータが表示されているアプリ画面

**複数の支払い受領方法に対応しているアプリの場合は見つけやすい場所に「iPhoneのタッチ決済」ボタンを配置する。** スクロールしなければボタンが表示されないようなデザインは避けてください。ほかの支払い受領手段に対応していない場合は、会計開始時に自動的に「iPhoneのタッチ決済」が開くようにします。

**「iPhoneのタッチ決済」とアプリの対応端末を簡単に切り替えられるようにする。** 「iPhoneのタッチ決済」への対応とBluetoothチップやPINカードリーダーなどの端末への対応は別物ですが、店舗が両方の手段を同時に設定できるようにして、ユーザ体験を効率化することができます。設定後には、アプリ設定を開くことなくその時々の会計に適した支払い受領手段を店舗が選択できるようにしてください。

**この機能をアクティベートするボタンのラベルには「iPhoneのタッチ決済」か、スペースが限られている場合は「タッチ決済」を使用する。** 例外は、「iPhoneのタッチ決済」が対応する唯一の支払い受領手段である場合です。その場合は、既存の請求ボタンや会計ボタンから「iPhoneのタッチ決済」がアクティベートされるようにしてもかまいません。複数の支払い受領手段に対応しており、それをアクティベートするボタンにアイコンを使用している場合は、「iPhoneのタッチ決済」ボタンに[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)の`wave.3.right.circle`または`wave.3.right.circle.fill`を使用します。「iPhoneのタッチ決済」ボタンには、Appleロゴを含めてはいけません。

![アイコンを含む「タッチ決済」ボタンの図。「iPhoneのタッチ決済」というテキストの前に波のシンボルが付いている、正しいボタンです。](https://docs-assets.developer.apple.com/published/5df49b7619561670c45747ba0e453f2d/tap-to-pay-on-iphone-symbol-correct%402x.png)

![丸に囲まれたチェックマークは正しい使い方を示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![アイコンを含む「タッチ決済」ボタンの図。「iPhoneのタッチ決済」というテキストの前にAppleロゴを使ってしまっている、正しくないボタンです。](https://docs-assets.developer.apple.com/published/a1e2f2006c784194e2b31544ea3233d4/tap-to-pay-on-iphone-logo-incorrect%402x.png)

![丸に囲まれた×印は不適切な使い方を示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

重要

「iPhoneのタッチ決済」ラベルは、支払いアクションにのみ使用します。支払い以外のアクションに使用できる言葉は、[その他の操作](/jp/design/human-interface-guidelines/tap-to-pay-on-iphone#Additional-interactions)を参照してください。

**「iPhoneのタッチ決済」ボタンがアプリのほかのボタンに一致するようにデザインする。** 上記のように「iPhoneのタッチ決済」または「タッチ決済」というラベルを使用する必要がありますが、ボタンにはインターフェイスに最も合うカラーと形状を使用できます。

**店舗側が「iPhoneのタッチ決済」を開始する前にアプリで顧客の最終支払い金額を決定する。** 例えばチップなど、顧客側で最終金額に影響する操作に対応しているアプリの場合は、「iPhoneのタッチ決済」画面を表示する前に店舗側がそうしたアクションを提示できるようにします。「iPhoneのタッチ決済」画面には、顧客が支払う最終的な金額を表示するようにします。

**会計フローで支払い前オプションに対応する場合は、「iPhoneのタッチ決済」画面の前に表示する。** 例えば、別の決済タイプを選択できる場合は、店舗が「iPhoneのタッチ決済」ボタンをタップしてから、「iPhoneのタッチ決済」画面を開くまでの間に、そのオプションを会計画面に表示できます。

## [結果の表示](/jp/design/human-interface-guidelines/tap-to-pay-on-iphone#Displaying-results)

顧客は、 _タップ_ によって支払いを行います。具体的には、アプリの「iPhoneのタッチ決済」画面に非接触カードまたはデジタルウォレットを近づける操作になります。タップが成功すると（必要な場合は、PIN入力にも成功する必要があります）、「iPhoneのタッチ決済」にチェックマークが表示され、アプリに暗号化された支払い情報（PSPに送信して処理するもの）を含むオブジェクトが渡されます。タップに失敗すると、「iPhoneのタッチ決済」にエラー画面が表示されます。タップに成功したときは、アプリに取引結果を表示する必要があります。失敗したときは、別の支払いオプションを提示します。

**取引は可能な限り早く処理する。** システムが提供しているAPIを使うと、「iPhoneのタッチ決済」画面でタップ完了を示すチェックマークのアニメーションが終わる前に、タップ成功の結果をリクエストできます。デベロッパ向けのガイダンスは、[`returnReadResultImmediately`](/documentation/ProximityReader/PaymentCardReader/Options-swift.struct/returnReadResultImmediately)を参照してください。

**取引結果画面の表示前、支払い承認中の間は、進行状況インジケータを表示する。** PSPと店舗のデバイスの両方のネットワーク接続などの要因により、取引の承認が完了するまでに、数秒かかる場合があります。スムーズな画面遷移を実現できるように、承認の[プログレスインジケーター](/jp/design/human-interface-guidelines/progress-indicators)は、「iPhoneのタッチ決済」画面のアニメーションが終わってから表示するようにします（デベロッパ向けのガイダンスは、[`PaymentCardReader.Event.readyForTap`](/documentation/ProximityReader/PaymentCardReader/Event/readyForTap)を参照してください）。

![アプリの会計画面の図。合計購入額の上に、不確定的な進行状況インジケータと「承認中」というテキストが表示されています。](https://docs-assets.developer.apple.com/published/6bbed8b345622947c84616a2392bca71/tap-to-pay-authorizing-payment%402x.png)

**取引の結果（拒否または成功）を明確に表示する。** 取引が拒否される原因としては、残高不足や不正利用の疑い、または顧客が間違ったPINを入力したときなどがあります。可能な限り、店舗がQRコードやテキストメッセージなどによるデジタル領収証を顧客に提示できるようにもしましょう。

![アプリの会計画面の図。合計購入額の上に緑色の丸に囲まれた緑色のチェックマークが表示されています。合計額の下には、「領収書オプションを選択」というテキストと、縦に並んだ3つのボタンが表示されています。](https://docs-assets.developer.apple.com/published/f07baff6e9b0755089b9464b7488fd90/tap-to-pay-confirmed-payment%402x.png)

![アプリの会計画面の図。合計購入額の上に、赤い丸に囲まれた赤いX印が表示されています。合計額の下には、「領収書オプションを選択」というテキストと、縦に並んだ3つのボタンが表示されています。](https://docs-assets.developer.apple.com/published/0d46cfbb32e301e4b873a3e4c8104384/tap-to-pay-unconfirmed-payment%402x.png)

**「iPhoneのタッチ決済」で支払いが完了できない場合でも、店舗が会計フローを完了できるようにする。** タップが失敗する可能性があるのは、カードが読み取れない場合、対応する支払いネットワークのカードでない場合、対象金額の取引が許可されていない場合、オンラインPIN入力を許可していない場合などです。このような場合は、以下の対応を行います:

  * 新しい画面を提示するか、会計画面を再利用して、店舗が別の形態の支払い（現金など）を受け入れられるようにする

  * 別の手段による会計に対応する（外部ハードウェアや支払いリンクなど）

  * 「iPhoneのタッチ決済」を再起動する（顧客が別のカードを試してみたい場合）

![アプリの会計画面の図。「支払いは完了していません」というテキストと合計購入額の上に、赤い丸に囲まれた赤いX印が表示されています。合計額の下には、「支払いオプションを選択」というテキストと、「iPhoneのタッチ決済」を含む4つのボタンがあります。](https://docs-assets.developer.apple.com/published/7c120b21c50d68baea88113703377d50/tap-to-pay-unsuccessful-transaction%402x.png)

支払い用カードのデータを受信したあと、以下に示すような状況が発生する場合もあります。このような状況が発生した場合は、PSPに連絡して対処方法についての指示に従ってください。

  * Strong Customer Authentication（SCA）の対応が必要になる地域もあります。その場合、タップ時にカードのPINが必須でなくても、カードを発行した銀行が、取引処理リクエストを受領したタイミングでPINをリクエストできます。この状況では、アプリで、取引結果ではなくPIN入力画面を表示することが必要な場合があります。

  * 一部の地域では、オフラインPINでの取引のように、一部のカードの制限に対処するため、アプリで追加要件を満たさなければならない場合があります。追加のPINフォールバック機能に対応し、タップから部分的なデータを収集するPSPもあります。その場合、店舗は、支払いリンクなどの別の手段で支払いを継続できます。

**店舗で対応しなければならないエラーが返される場合は、問題を分かりやすく説明して、推奨される適切な解決策を表示する。** 例えば、デバイスのiOSが「iPhoneのタッチ決済」に対応していないバージョンだった場合は、最新バージョンへのアップデートを推奨する[アラート](/jp/design/human-interface-guidelines/alerts)を表示します。デベロッパ向けのガイダンスは、[`PaymentCardReaderSession.ReadError`](/documentation/ProximityReader/PaymentCardReaderSession/ReadError)を参照してください。

**店舗が解決できない問題について、簡単にサポートを得られるようにする。** 例えば、店舗をアプリのヘルプコンテンツやWebサイトに誘導し、サポートチームに連絡できるアクションを提供します。

## [その他の操作](/jp/design/human-interface-guidelines/tap-to-pay-on-iphone#Additional-interactions)

店舗は、金銭の取引がない場合でも、「iPhoneのタッチ決済」を使って支払い用カードを読み取ることができます。これにより、過去の取引を照会する、今後の支払いのためにカード情報を保持する、払い戻しを行う、顧客情報を確認するなどのユースケースに対応できます。

**金銭の取引がない場合に、「iPhoneのタッチ決済」画面を開いて支払い用カードを読み取るボタンには、一般的なラベルを使用する。** このようなラベルには、「iPhoneのタッチ決済」や「タッチ決済」を含めずに、「照会」、「カードの保存」、「確認」、「払い戻し」などの一般的なラベルを使用します。

顧客のAppleウォレットにその他のNFC対応のカードまたはパス（メンバーカード、割引カード、ポイントカードなど）がある場合は、支払い用カードと同時に読み取ることも、個別に読み取ることもできます。

**アプリがポイントカードのみでの取引に対応している場合は、そのフローと「iPhoneのタッチ決済」を使用する支払い受領フローとを明確に分ける。** ポイントカードでの取引を開始することを明記した別のボタンを用意するとよいでしょう。店舗がボタンを押し間違えるのを防ぐため、ポイント取引のボタンのラベルに「iPhoneのタッチ決済」や「タッチ決済」などの支払い関連の用語を含めないようにします。

![「ポイントカード」というラベルが付いたボタンの図。](https://docs-assets.developer.apple.com/published/a832806fc00d2928ec7a982a53baa63f/loyalty-card%402x.png)

![丸に囲まれたチェックマークは正しい使い方を示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![「iPhoneのタッチ決済、ポイント」というラベルが付いたボタンの図。](https://docs-assets.developer.apple.com/published/08cc008e9526a6f022712ecafb2909d1/tap-to-pay-on-iphone-loyalty%402x.png)

![丸に囲まれた×印は不適切な使い方を示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/tap-to-pay-on-iphone#Platform-considerations)

 _iOSに追加の考慮事項はありません。iPadOS、macOS、tvOS、visionOS、watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/tap-to-pay-on-iphone#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/tap-to-pay-on-iphone#Related)

[「iPhoneのタッチ決済」マーケティングガイドライン](https://developer.apple.com/tap-to-pay/marketing-guidelines/)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/tap-to-pay-on-iphone#Developer-documentation)

[アプリで「iPhoneのタッチ決済」に対応する](/documentation/ProximityReader/adding-support-for-tap-to-pay-on-iphone-to-your-app) — ProximityReader

## [変更履歴](/jp/design/human-interface-guidelines/tap-to-pay-on-iphone#Change-log)

日付| 変更内容  
---|---  
2024年1月17日| 店舗教育のガイダンスを更新。  
2024年5月07日| 機能の有効化および店舗への教育に関するガイダンスを追加するために更新。  
2023年3月03日| 店舗への教育や体験向上のためのガイダンスを改善しました。  
2022年9月14日| 「iPhoneのタッチ決済」の準備、店舗が機能の利用方法を習得するためのガイダンスを改訂しました。
