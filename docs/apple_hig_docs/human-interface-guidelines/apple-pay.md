# Apple Pay

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/apple-pay

# Apple Pay

Apple Payは、物理的な商品やサービス、さらには寄付やサブスクリプションの支払いなどを安全かつ簡単に行う手段です。iPhone、iPad、Mac、Apple Vision Pro、Apple Watchで動作するアプリ、Webサイト、および任意のブラウザで利用できます。

![ドル記号のスケッチ。Apple Payを示しています。画像の上に長方形と円形のグリッド線が重ねられており、画像全体が6色の初代Appleロゴの青色を連想させる青みを帯びています。](https://docs-assets.developer.apple.com/published/8f0a23ba8866347ebfe2cbef68186b7e/technologies-Apple-Pay-intro%402x.png)

ユーザは、デバイスに安全に保存されている認証資格情報を使用して支払いを承認し、配送や連絡先に関する情報を提供します。

ヒント

Apple Payと[アプリ内課金](/jp/design/human-interface-guidelines/in-app-purchase)の違いを理解することが重要です。Apple Payは、アプリ内で食料品、衣類、電気器具といった物理的な商品や、クラブの会員権、ホテルの予約、イベントチケットなどのサービスを販売する場合、または寄付を行う場合に使用します。アプリ内課金は、アプリのプレミアムコンテンツなどのバーチャル商品や、デジタルコンテンツのサブスクリプションを販売する場合に使用します。

Apple Payに対応するアプリやWebサイトでは、利用可能な支払いオプションとしてApple Payを表示し、タップでペイメントシートが開くApple Payボタンを購入フローに含めます。会計時には、Apple Payにリンクされたクレジットカードまたはデビットカード、購入金額（税と手数料を含む）、配送オプション、連絡先情報をペイメントシートに表示できます。ユーザは、必要な調整を行ってから、支払いを承認して購入手続きを完了します。デベロッパ向けのガイダンスは、[Apple Pay](/documentation/PassKit/apple-pay)を参照してください。

Apple Payを提供するすべてのWebサイトには、プライバシーステートメントを含める必要があります。また、[Web上のApple Payの利用に関するガイドライン](https://developer.apple.com/apple-pay/acceptable-use-guidelines-for-websites/)を順守する必要があります。デベロッパ向けのガイダンスは、[Apple Pay on the Web](/documentation/ApplePayontheWeb)を参照してください。WebでのApple Payの体験型デモは、[WebでのApple Payのインタラクティブデモ](https://applepaydemo.apple.com)を参照してください。

![ペイメントシートのスクリーンショット。銀行情報、配送先住所、合計金額など、詳しい購入情報が表示されています。](https://docs-assets.developer.apple.com/published/fe7f912bd6f264646636c2f65bdf0e9d/apple-pay-sheet%402x.png)

デバイスがFace ID、Touch ID、またはOptic IDに対応していれば、ほとんどの場合、デバイスは支払い認証を行います。場合によっては、支払い認証は安全なBluetooth接続またはスキャン可能なコードを経由して、近くのiPhone、iPad、またはApple Watchに転送されます。

![左にMacBook Pro、右にiPhoneがある図。MacBook ProのSafariウインドウに表示されたオンラインストアに、Apple Payで購入に進むボタンと、バッグに追加するためのボタンが表示されています。iPhoneにはApple Payのペイメントシートが表示されています。](https://docs-assets.developer.apple.com/published/77f95bf8ef51e845e069f8995d2e2258/apple-pay-hero%402x.png)

## [Apple Payの提供](/jp/design/human-interface-guidelines/apple-pay#Offering-Apple-Pay)

**対応するすべてのデバイスとブラウザでApple Payを提供する。** Apple Payに対応していないデバイスには、支払いオプションとしてApple Payを表示しないようにします。デバイスがApple Payに対応しているかどうかを判定するには、Apple Pay APIを使用してください。デベロッパ向けのガイダンスは、[`PKPaymentAuthorizationController`](/documentation/PassKit/PKPaymentAuthorizationController)（iOS、watchOS）および[`canMakePayments`](/documentation/ApplePayontheWeb/ApplePaySession/canMakePayments)（Web）を参照してください。

**Apple Pay APIを使用してウォレットに有効なカードがあるかどうかを確認する場合は、APIを使用するすべての場所でApple Payをプライマリの支払いオプションにする（唯一のオプションにする必要はない）。** 例えば、ほかのオプションとあわせて表示するときに、Apple Payの支払いオプションをあらかじめ選択した状態にします。デベロッパ向けのガイダンスは、[アプリでApple Payを提供する](/documentation/PassKit/offering-apple-pay-in-your-app)（iOS、watchOS）および[Apple Payの利用状況の確認](/documentation/ApplePayontheWeb/checking-for-apple-pay-availability)（Web）を参照してください。

**ほかの支払い方法も提示する場合はApple Payも同じ場所に提示する。** 支払い方法を提示または受け付けるすべてのページや画面で、少なくともApple Payがほかの支払いオプションに比べて目立たなくならないようにしてください。

**Apple PayボタンからApple Payの支払い処理を開始する場合は、必ずAppleが提供するAPIを使用して表示する。** ボタンのグラフィックスとは違い、APIが生成するボタンは常に適切な見た目になり、自動的にローカライズされます。

**カスタムのボタンを使用してApple Payの支払い処理を開始する場合は、カスタムボタンに「Apple Pay」やApple Payロゴを表示しない。** この場合にApple Payが利用できることを伝えるには、支払いボタンを表示するページにApple Payマークを表示するか、そのページ内のテキストでApple Payに言及してください。

![正しい表示方法を示した図。Apple Payロゴの下にあるカスタムボタンのタイトルが「注文する」になっています。](https://docs-assets.developer.apple.com/published/51d459ff0395013adb94878486246a4f/custom-button-yes%402x.png)

![正しい使用法](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![正しくない表示方法を示した図。Apple Payロゴの下にあるカスタムボタンのタイトルが「Apple Pay」になってしまっています。](https://docs-assets.developer.apple.com/published/2e0976c8eab0c40ed835d74394cc65dc/custom-button-no%402x.png)

![正しくない使用法](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

**Apple PayボタンはApple Payでの支払い処理を開始する場合にのみ使用する（適宜Apple Payの設定処理を開始するのは可）。** 購入時にApple Payボタンを選択したユーザのデバイスでApple Payが設定されていなかった場合は、Apple Pay設定画面が表示されます。Apple Payボタンは、これ以外の方法では使用しないでください。

**Apple Payボタンを非表示にしたり、使用できないように見せたりしない。** 商品のサイズや色が選択されていないなど、まだApple Payボタンが使用できない状態のときは、ボタンがタップまたはクリックされた段階で問題を指摘してください。

**Apple PayマークはApple Payを利用できることを伝えるためだけに使用する。** Apple Payマークは支払いを促進するものではありません。絶対に、支払いボタンとして使用したり、ボタンとして配置したりしないでください。Apple Payが支払い方法として選択されていることを示すためにApple Payマークを使用したい場合は、Apple Payの支払いを開始するカスタムボタンをアプリのデザインに合わせて別途作成します。

**WebサイトでApple Payが利用できることを検索エンジンに知らせる。** Webサイトでセマンティックマークアップを使用して商品の詳細情報を検索エンジンに知らせている場合は、支払いオプションにApple Payを含めます。

アプリデベロッパ向けのガイダンスは、[Apple Pay](/documentation/PassKit/apple-pay)を参照してください。WebでApple Payを利用できるかどうかを判断する方法など、Webサイトデベロッパ向けのガイダンスは、[Apple Pay on the Web](/documentation/ApplePayontheWeb)を参照してください。

## [チェックアウトの効率化](/jp/design/human-interface-guidelines/apple-pay#Streamlining-checkout)

**まとまりのあるチェックアウト体験を提供する。** チェックアウトフロー全体がアプリやWebサイトと一体化しているように感じられるのが理想です。一体感を強く印象づけるには、チェックアウトフロー全体をブランディングすると共に、別のページやウインドウが開かないようにします。特にWebサイトのチェックアウトフローでは、手続き中に新しいウインドウが開くと、ユーザが戸惑い、別のWebサイトに飛ばされたと感じてしまうかもしれません。

**Apple Payが使用可能な場合はユーザがその使用を希望していることを前提にする。** Apple Payボタンを支払いオプションの1番目として表示してほかのオプションよりも大きくするか、区切り線を引いてほかの支払いオプションと視覚的に分けることを検討してください。

**商品詳細ページにApple Payボタンを配置して単品を素早く購入できるようにする。** ショッピングカートに入れるオプションのほかに、商品詳細ページにApple Payボタンを追加して個々の商品を素早く購入できるようにすることを検討しましょう。このボタンから購入に進んだ場合に購入できるのは単品のみとし、その時点でショッピングカートに入っていたものは支払いから除外する必要があります。商品詳細ページから直接購入した商品がショッピングカートに入っていた場合は、購入の完了後にその商品をカートから削除してください。

**エクスプレスチェックアウトで複数品目を素早く購入できるようにする。** ペイメントシートを即座に表示するエクスプレスチェックアウト機能の提供を検討してください。こうすることで、複数の品物を1つの配送方法と配送先にまとめて素早く購入できるようになります。クーポンやプロモーションコードを提供している場合は、ペイメントシートに入力できるようにチェックアウトの体験を拡張できます。

**色やサイズのオプションなどの必要な情報はApple Payボタンの操作に進む前に収集する。** ユーザがオプションを選択し忘れた場合など、購入に進む際に追加情報が必要な場合は、問題を指摘して修正を促してください。ハイライトや警告テキストを使用して不足している情報が分かるようにし、問題のフィールドに自動的に移動することで、ユーザが素早く修正して購入を完了できるようにします。

**省略可能な情報は購入に進む前に収集する。** ギフトメッセージや配送指示などの省略可能なデータは、ペイメントシートでは入力できないので、事前に収集します。あるいは購入後でもかまいません。

**配送方法と配送先が複数ある場合は、ペイメントシートを表示する前に収集する。** ペイメントシートでは、注文全体に対して1つの配送方法と1つの配送先しか選択できません。注文する商品ごとに配送方法と配送先を選べるようにしている場合は、ペイメントシート上ではなく、Apple Payでの注文に進む前にこれらの情報を収集してください。

**店舗受け取りの場合は、ペイメントシートを表示する前に受け取り場所を選べるようにする。** 希望の受け取り場所が選択されたら、読み取り専用フォーマットでペイメントシートに受け取り場所の住所を表示します。デベロッパ向けのガイダンスは、[読み取り専用の受け取り場所の表示](/documentation/PassKit/displaying-a-read-only-pickup-address)を参照してください。

**Apple Payの情報を優先する。** Apple Payの情報は完全かつ最新であると考えてください。連絡先、配送、支払いに関する情報がアプリやWebサイトにすでにある場合でも、訂正が生じる可能性が減るように会計時にApple Payの最新情報を取得することを検討してください。

**購入前のアカウント作成を必須としない。** ユーザにアカウント登録をしてもらいたい場合は、注文確認ページで登録を促します。会計時にペイメントシートに入力された情報を使用し、できる限り多くの登録フィールドを事前入力しておきましょう。

![iPhoneの注文確認画面の図。アカウントを作成するボタンとApple Payでサインアップするボタンが表示されています。](https://docs-assets.developer.apple.com/published/9ed64eee0d7cc1b4377336a06aaed9e2/payment-sheet-before-account%402x.png)

**取引結果をペイメントシートに表示する。** 取引ができなかった場合は、ユーザが問題を修正できるようにペイメントシートにエラーを表示できます。

**注文確認ページまたは注文完了ページを表示する。** ペイメントシートに取引の結果を表示したあと、注文の確認と感謝のメッセージを表示します。この画面には、注文の出荷見込みや配送状況の確認方法に関する情報も含めてください。確認ページに「Apple Pay」と表示することは必須ではありませんが、表示する場合は、決済に使われた口座の最後の4桁のあとに表示するか、別途備考として表示します。例えば、「1234（Apple Pay）」や「Apple Payでの支払い」とします。

### [ペイメントシートのカスタマイズ](/jp/design/human-interface-guidelines/apple-pay#Customizing-the-payment-sheet)

**不可欠な情報のみ表示およびリクエストする。** ペイメントシートに不必要な情報が含まれていると、ユーザが戸惑ったり、プライバシーについて不安を感じたりする可能性があります。例えば、電子的に配信されるギフトカードの購入画面に連絡先メールアドレスが表示されるのは分かりますが、配送先住所まで表示されるのは不自然です。このような場合に配送先住所を表示したり要求したりすると、実体のあるものが配送されるような誤った印象を与える可能性があります。

**有効なクーポンやプロモーションコードを表示するか、ユーザが入力できる手段を提供する。** 例えば、ペイメントシートの表示前にコードが入力できるようになっている場合は、シートにもコードを表示するようにすれば、ユーザはコードがきちんと適用されているという安心を得られます。あるいは、ペイメントシートでコードを入力できるようにすると、エクスプレスチェックアウトフローでは特に便利かもしれません。

**ペイメントシートで配送方法を選べるようにする。** スペースが許す限り、明確な説明と価格を表示し、適宜、利用できる各オプションについて配送予定日または受け取り可能日（または期間）を表示します。iOS 15以降では、配送方法のカレンダーやタイムゾーン対応を利用して、ユーザの現在地によらず、正確な配送または受け取りの情報を提供できます。デベロッパ向けのガイダンスは、[`PKDateComponentsRange`](/documentation/PassKit/PKDateComponentsRange)を参照してください。

**店舗受け取りの場合は、都合のよい受け取り時間帯を選べるようにすることを検討する。** 配送方法から、日付や時間帯を選べるようにすることができます。

**明細項目を、追加料金、割引、未決済金額、追加寄付、定期購入、後払いを説明するために使用する。** 明細項目にはラベルと価格を含めることができ、定期購入の支払いの明細項目には頻度も追加できます。明細項目を購入商品の箇条書きに使用しないでください。デベロッパ向けのガイダンスは[`paymentSummaryItems`](/documentation/PassKit/PKPaymentRequest/paymentSummaryItems)を参照してください。寄付についてのガイダンスは[寄付への対応](/jp/design/human-interface-guidelines/apple-pay#Supporting-donations)を参照してください。

![アプリ内ペイメントシートのスクリーンショット。ギフトラッピングの追加費用と、クーポンで適用されるクレジットが含まれています。](https://docs-assets.developer.apple.com/published/6531113f7ff3a0e85e0011e2382369e4/payment-sheet-ios%402x.png)

![Webページのペイメントシートのスクリーンショット。ギフトラッピングの追加費用と、クーポンで適用されるクレジットが含まれています。](https://docs-assets.developer.apple.com/published/73ad2652d0359fb22deeface24659419/payment-sheet-web%402x.png)

**明細項目は短くする。** 明細項目は具体的に記し、一目で簡単に理解できるようにします。可能な場合は、明細項目を1行に収めます。

**合計と同じ行の _「へ支払い」_ という単語の前に企業名を表示する。**銀行やクレジットカードの明細に表示される請求元と同じ企業名を使用します。こうすれば、ユーザは支払い先が正しいという安心を得られます。例えば、「[_企業名_]へ支払い」のようにします。

**自社が最終販売者でない場合は、ペイメントシートに自社名と最終販売者の名前の両方を表示する。** アプリやApp Clip、Webサイトで、自社と関係のない最終販売者から購入できるようにすることもあるでしょう。これには、例えばマーケットプレイスのアプリでユーザの知らない最終販売者から商品を購入できるようにしたり、実店舗のレジに並ばずに会計を済ませることができるセルフチェックアウトサービスをアプリで提供したりするなど、いくつかのパターンが考えられます。このような場合、ユーザは2つの企業が取引に関わっていることに気付かないかもしれません。そのため、両方の企業名を明示し、それぞれの役割を明確にすることが不可欠です。最終販売者の仲介役を果たすアプリでは、ペイメントシートの支払い行でその旨を明確かつ簡潔に説明します。例えば、「[_最終販売者企業名_ （ _自社名_ 経由）]へ支払い」のようにします。

**支払いの承認後に追加費用が発生する可能性がある場合は明確に開示する。** 場合によっては、会計の時点では合計金額が判明しないことがあります。例えば、距離制運賃や時間制運賃が適用される送迎サービスでは、会計後に金額が変わるかもしれません。または、商品の配達後にチップを払いたいユーザもいるでしょう。現地の規制で許されている場合、このようなケースでは、明確な説明に加え、「未決済金額」と表記した小計をペイメントシートに表示します。特定の金額を事前承認している場合は、ペイメントシートにその情報を正確に反映させてください。

**データ入力と支払いのエラーに適切に対処する。** 会計中にエラーが発生した場合は、ユーザが素早く問題を解決して取引を完了できるようにしてください。関連するガイダンスは、[データの検証](/jp/design/human-interface-guidelines/apple-pay#Data-validation)を参照してください。

### [Webサイトのアイコンの表示](/jp/design/human-interface-guidelines/apple-pay#Displaying-a-website-icon)

Webサイトなら、おそらく、ブックマークやURLフィールド、デバイスのホーム画面に表示する用のアイコンがあるでしょう。Apple Payに対応したWebサイトでは、サマリービューと、支払いの承認に使われる接続済みデバイスのペイメントシートにこのアイコンを表示できます。アイコンが表示されていれば、ユーザは支払い先が正しいという安心を得られます。

WebサイトがApple Payに対応している場合、サマリービューとペイメントシートで使用するアイコンは以下のサイズにしてください。

@2x| @3x  
---|---  
60x60 pt（120x120 px @2x）| 60x60 pt（180x180 px @3x）  
  
![iPhoneのApple Payペイメントシートの図。支払い情報の上にWebサイトのアイコンが表示されています。](https://docs-assets.developer.apple.com/published/29d747cfb219330c1c6364d099ee3d5a/web-icon-payment%402x.png)

## [エラーの処理](/jp/design/human-interface-guidelines/apple-pay#Handling-errors)

会計中や支払い処理中に問題が発生した場合は、ユーザが素早く問題を解決して取引を完了できるように、明確で即効性のある指示を出しましょう。

### [データの検証](/jp/design/human-interface-guidelines/apple-pay#Data-validation)

アプリやWebサイトは、ペイメントシートが表示されるとき、ペイメントシートの特定のフィールド値が変更されたときや、取引が承認されたあとに、ユーザの入力に応答することができます。これらの機会を利用して、データ入力の問題をチェックしたり、明確で一貫性のある文言を表示したりしてください。

![iPhoneのアプリ内Apple Payペイメントシートのスクリーンショット。配送先住所のエラーが表示されています。](https://docs-assets.developer.apple.com/published/2d43c45c73c7184ffdaa8980a6b6add9/pay-sheet-error-ios%402x.png)

ペイメントシートのエラーメッセージ

![iPhoneのアプリ内配送画面のスクリーンショット。郵便番号が自宅住所の市区町村と一致していないことが示されています。別の配送先住所を選択または追加するオプションがあります。](https://docs-assets.developer.apple.com/published/aef7fe4006ce2c006a3201079b008d16/detail-view-error-ios%402x.png)

カスタム詳細ビューのエラーメッセージ

![WebページのApple Payペイメントシートのスクリーンショット。配送先住所のエラーが表示されています。](https://docs-assets.developer.apple.com/published/0ceb724a53b0a46f24e1ef4484ce9a75/pay-sheet-error-web%402x.png)ペイメントシートのエラーメッセージ

![WebページのApple Payペイメントシートのスクリーンショット。配送先住所のエラーが表示されています。ペイメントシート上に表示されたオーバーレイに、郵便番号が自宅住所の市区町村と一致していないことが示されています。別の配送先住所を選択するか配送先住所を編集するオプションがあります。](https://docs-assets.developer.apple.com/published/d7e2517f0774f9fe9176cc724f5d9a01/detail-view-error-web%402x.png)カスタム詳細ビューのエラーメッセージ

データが無効な場合、ペイメントシートの問題のフィールドを確認するよう求めるエラーメッセージがシステムによって表示されます。ここでフィールドを選択すると、詳しい情報を確認して問題を解決することができます。問題のフィールドが選択されたときに表示される詳細ビューには、カスタムのエラーメッセージを提供してください。

デベロッパ向けのガイダンスは、[`PKPaymentAuthorizationViewControllerDelegate`](/documentation/PassKit/PKPaymentAuthorizationViewControllerDelegate)（iOS、watchOS）および[Apple Pay on the Web](/documentation/ApplePayontheWeb)（Web）を参照してください。

注意

プライバシー上の理由から、ユーザが取引の承認を試みるまでは、アプリやWebサイトからアクセスできるデータが制限されます。承認前の段階でアクセスできるのは、カードのタイプと部分的な配送先住所のみです。承認に失敗したときにエラーを表示することは不可欠ですが、可能な限り、承認前に利用できる情報を検証し、問題を報告する必要があります。

**ビジネスロジックを押しつけない。** 関係のないデータを無視し、欠けているデータを推測できるスマートなデータ検証手順を設計しましょう。例えば、米国の5桁の郵便番号が必要な場面で、ユーザが追加の4桁の番号（ZIP+4コード）を入力した場合は、訂正を求めるのではなく、追加の桁を無視します。電話番号は複数の形式で入力できるようにし、例えばハイフンや国コードがあってもなくてもエラーにならないようにします。

**システムに正確なステータスを報告する。** 問題が発生した場合は、ペイメントシートに最も関連性の高いエラーメッセージが表示されるように、アプリやWebサイトで正確に問題のタイプを示す必要があります。これは、カスタムエラーメッセージと一緒に正確なステータスコードを渡すことで行います。デベロッパ向けのガイダンスは、[`PKPaymentError`](/documentation/PassKit/PKPaymentError)（iOS、watchOS）および[Apple Payステータスコード](/documentation/ApplePayontheWeb/apple-pay-status-codes)（Web）を参照してください。

**データが無効な場合やフォーマットが正しくない場合は問題を簡潔かつ具体的に示す。** 該当のフィールドと、具体的に求めていることを示します。例えば、入力された郵便番号が無効な場合は、「住所が無効です」ではなく、「郵便番号が市区町村と一致しません」のような具体的なメッセージを表示します。配送先住所が対象地域でない場合は、「この州には配送できません」のようなメッセージで理由を説明します。センテンススタイルの大文字化を使って名詞句にし、文末記号は付けません。メッセージが切れることのないように、なるべく全角64文字以下にします。

### [支払いの処理](/jp/design/human-interface-guidelines/apple-pay#Payment-processing)

**中断に適切に対処する。** キャンセルなどのユーザによるイベントや、タイムアウトなどのシステムによるイベントによって支払いフローが中断され、ペイメントシートが閉じられる場合があります。このようなイベントが発生した場合は、処理中の支払いをすべてキャンセルする必要があります。ペイメントシートが閉じても、再度Apple Payボタンを選択すれば処理をやり直すことができます。デベロッパ向けのガイダンスは、[`PKPaymentAuthorizationViewControllerDelegate`](/documentation/PassKit/PKPaymentAuthorizationViewControllerDelegate)（iOS、watchOS）および[`oncancel`](/documentation/ApplePayontheWeb/ApplePaySession/oncancel)（Web）を参照してください。

## [サブスクリプションへの対応](/jp/design/human-interface-guidelines/apple-pay#Supporting-subscriptions)

アプリやWebサイトでは、Apple Payを使用して定期購入の承認を求めることができます。定期購入は、月額制の映画チケットのサブスクリプションのように固定額にすることも、毎週の食料品の注文のように変動させることもできます（規制で禁止されていない地域の場合）。初回の承認には、割引や追加料金を含めることもできます。

![固定額のサブスクリプションを示すアプリ内Apple Payペイメントシートのスクリーンショット。月額が表示されています。](https://docs-assets.developer.apple.com/published/a308117aabe00d5897bd1b03232d3823/fixed-subscription-ios%402x.png)

固定額のサブスクリプション

![変動額のサブスクリプションを示すアプリ内Apple Payペイメントシートのスクリーンショット。「未決済金額」というテキストが表示されています。](https://docs-assets.developer.apple.com/published/92a769e20ad2a31554747cd7f53b3b29/variable-subscription-ios%402x.png)

変動額のサブスクリプション（規制で禁止されていない地域の場合）

![固定額のサブスクリプションを示すWebページのApple Payペイメントシートのスクリーンショット。月額が表示されています。](https://docs-assets.developer.apple.com/published/da174f5f88d93865b1bce60758ca8579/fixed-subscription-web%402x.png)固定額のサブスクリプション

![変動額のサブスクリプションを示すWebページのApple Payペイメントシートのスクリーンショット。「未決済金額」というテキストが表示されています。](https://docs-assets.developer.apple.com/published/3014421ef0223102e18b87fe15786073/variable-subscription-web%402x.png)変動額のサブスクリプション（規制で禁止されていない地域の場合）

**ペイメントシートを表示する前にサブスクリプションの詳細を明示する。** 定期購入の支払い承認を求める前に、課金の頻度などの利用規約をユーザが完全に理解できるようにします。課金の頻度はペイメントシートでも再度表示します。

**課金の頻度、割引、前払いの追加料金を再度説明する明細項目を含める。** これらの明細項目を使用して、承認の内容をあらためて伝えます。承認時に支払いが必要ない場合は、課金のタイミングを明確に示してください。

![固定額のサブスクリプションを示すアプリ内Apple Payペイメントシートのスクリーンショット。このサブスクリプションでは、初月は支払いが発生しません。合計金額に0ドルと表示されています。](https://docs-assets.developer.apple.com/published/2d1e4f4dc202f88f24c55578327a541b/no-payment-required-ios%402x.png)

承認時に支払いが必要ない場合

![固定額のサブスクリプションを示すWebページのApple Payペイメントシートのスクリーンショット。このサブスクリプションでは、初月は支払いが発生しません。合計金額に0ドルと表示されています。](https://docs-assets.developer.apple.com/published/a630d12908a02293ea1219c68e943d9e/no-payment-required-web%402x.png)承認時に支払いが必要ない場合

**合計行で現在の支払金額を明示する。** 承認時に課金される金額が分かるようにします。

**サブスクリプションの変更で追加料金が発生する場合のみペイメントシートを表示する。** サブスクリプションを変更しても、料金が下がる場合や変わらない場合なら、承認は必要ありません。

### [寄付への対応](/jp/design/human-interface-guidelines/apple-pay#Supporting-donations)

[承認済み非営利団体](https://developer.apple.com/support/apple-pay-nonprofits/)は、Apple Payで寄付を受け取ることができます。

**明細項目を使用して寄付であることを明示する。** 寄付を承認しようとしていることが分かるように、ペイメントシートに明細項目を表示します。例えば、「寄付$50.00」と表示します。

**スムーズに会計できるように寄付額をあらかじめ設定しておく。** $25、$50、$100のような寄付額の案をワンステップで選択できるようにしておけば、寄付の手順が減ります。ただし、寄付額を自由に変えられるように、必ず「その他の金額」オプションも含めてください。

## [Apple Payボタンの使用](/jp/design/human-interface-guidelines/apple-pay#Using-Apple-Pay-buttons)

システムでは、アプリやWebサイトで使用できるさまざまなタイプやスタイルのApple Payボタンが用意されています。Apple Payボタンとは異なり、[Apple Payマーク](/jp/design/human-interface-guidelines/apple-pay#Apple-Pay-mark)は、支払いにApple Payを利用できることを示すために使用します。

独自にApple Payボタンをデザインしたり、システムが提供しているデザインを模倣しようとしたりしないでください。

デベロッパ向けのガイダンスは、[`PKPaymentButtonType`](/documentation/PassKit/PKPaymentButtonType)および[`PKPaymentButtonStyle`](/documentation/PassKit/PKPaymentButtonStyle)（iOS、macOS）、[`WKInterfacePaymentButton`](/documentation/WatchKit/WKInterfacePaymentButton)（watchOS）、および[Apple Pay on the Web](/documentation/ApplePayontheWeb)（Web）を参照してください。

### [ボタンのタイプ](/jp/design/human-interface-guidelines/apple-pay#Button-types)

Appleが提供しているボタンには複数のタイプがあるので、購入処理や支払い処理で使用される用語やフローに最も適したボタンのタイプを選択できます。

Apple Payボタンの作成には、Appleが提供するAPIを使用してください。システムが提供するAPIを使用すると、以下が可能になります:

  * Appleが承認したキャプション、フォント、カラー、スタイルが確実に使用される

  * サイズを変更してもボタンのコンテンツの理想的な比率が保たれる

  * ボタンのキャプションが、デバイスで設定されている言語のものに自動的に切り替わる

  * ボタンの角丸半径をUIのスタイルに一致させるよう設定できる

  * VoiceOverがボタンを説明する際に使用する代替テキストラベルがシステムによって提供される

支払いボタンのタイプ| 使用例  
---|---  
![「Apple Payで購入」ボタン](https://docs-assets.developer.apple.com/published/acd33725d072693deaebf71f64840b22/button-buy-with%402x.png)| 商品詳細ページやショッピングカートのページなど、アプリやWebサイト内の購入ができる領域。  
![「Apple Payで支払う」ボタン](https://docs-assets.developer.apple.com/published/6b711b41f048b2dbf7e84ca7884a9953/button-pay-with%402x.png)| 公共料金（ケーブルテレビや電力など）やサービス代金（配管や自動車修理など）などの支払いを行うアプリやWebサイト。  
![「Apple Payで購入に進む」ボタン](https://docs-assets.developer.apple.com/published/5b6b2329e4ed3f67b576caa1a5e99bea/button-check-out-with%402x.png)| 「 _で購入に進む_ 」というテキストを含む支払いボタンがほかにもあるショッピングカートや購入オプションを提供するアプリやWebサイト。  
![「Apple Payで続ける」ボタン](https://docs-assets.developer.apple.com/published/a7f46875718c19fd1606e06479d0934b/button-continue-with%402x.png)| 「 _で続ける_ 」というテキストを含む支払いボタンがほかにもあるショッピングカートや購入オプションを提供するアプリやWebサイト。  
![「Apple Payで予約」ボタン](https://docs-assets.developer.apple.com/published/57a69988e311ea0c2a39b2a201de765e/button-book-with%402x.png)| フライトや旅行などを予約できるアプリやWebサイト。  
![「Apple Payで寄付」ボタン](https://docs-assets.developer.apple.com/published/639e290c1849386d98c6f5ad1dfbd1a8/button-donate-with%402x.png)| [承認済み非営利団体](https://developer.apple.com/support/apple-pay-nonprofits/)への寄付を行えるアプリやWebサイト。  
![「Apple Payでサブスクリプション」ボタン](https://docs-assets.developer.apple.com/published/75baa27c9ea7e33fb3bd8f2062b66a3a/button-subscribe-with%402x.png)| ジムの会員権やミールキットの配送サービスなど、サブスクリプションを購入できるアプリやWebサイト。  
![「Apple Payでチャージ（Reload with Apple Pay）」ボタン](https://docs-assets.developer.apple.com/published/decae3e5d32c1c5f5f5557faa4c6dff7/button-reload-with%402x.png)| （Reload with Apple Pay）交通機関やプリペイド電話プランなどのサービスに関連付けられたカードや口座、支払いシステムに残高を追加することができ、それに関して _チャージ_ （Reload）という用語を使用しているアプリやWebサイト。  
![「Apple Payでチャージ（Add Money with Apple Pay）」ボタン](https://docs-assets.developer.apple.com/published/c78d847683a97164825fa43ef84ee4e6/button-add-money-with%402x.png)| （Add Money with Apple Pay）交通機関やプリペイド電話プランなどのサービスに関連付けられたカードや口座、支払いシステムに残高を追加することができ、それに関して _チャージ_ （Add Money）という用語を使用しているアプリやWebサイト。  
![「Apple Payでチャージ（Top Up with Apple Pay）」ボタン](https://docs-assets.developer.apple.com/published/b02e32beaa4987cd1d3729d07b3b1850/button-top-up-with%402x.png)| （Top Up with Apple Pay）交通機関やプリペイド電話プランなどのサービスに関連付けられたカードや口座、支払いシステムに残高を追加することができ、それに関して _チャージ_ （Top Up）という用語を使用しているアプリやWebサイト。  
![「Apple Payで注文」ボタン](https://docs-assets.developer.apple.com/published/ab3c33297a46c1aee7bfa662b99c9ffa/button-order-with%402x.png)| 食事や花などの品物を注文できるアプリやWebサイト。  
![「Apple Payでレンタル」ボタン](https://docs-assets.developer.apple.com/published/6816dc44e0f9d498055b59528bfcaa6b/button-rent-with%402x.png)| 自動車やスクーターなどの品物をレンタルできるアプリやWebサイト。  
![「Apple Payで支援」ボタン](https://docs-assets.developer.apple.com/published/b058caa1223f8b9407d24e5d145c93c6/button-support-with%402x.png)| プロジェクト、活動、団体などに資金提供をすることができ、それに関して _支援_ という用語を使用しているアプリやWebサイト。  
![「Apple Payで献金」ボタン](https://docs-assets.developer.apple.com/published/f1bec9fd7795c068dfd97acec778905d/button-contribute-with%402x.png)| プロジェクト、活動、団体などに資金提供をすることができ、それに関して _献金_ という用語を使用しているアプリやWebサイト。  
![「Apple Payでチップ」ボタン](https://docs-assets.developer.apple.com/published/d04f0fb35ae340f0c7adf5a615f7b0ac/button-tip-with%402x.png)| 品物やサービスに対してチップを渡せるアプリやWebサイト。  
![「Apple Pay」ボタン](https://docs-assets.developer.apple.com/published/5bab746e63536c6f8d3eaf09d269ad40/ap-button%402x.png)| スタイル上の理由でボタンの最小幅をもっと狭くしたいアプリやWebサイト。特定の行動喚起を行わないボタンを使用したいアプリやWebサイト。アプリやWebサイトが動作しているオペレーティングシステムが対応していないタイプの支払いボタンを選択した場合は、自動的にこのボタンに置き換わることがあります。  
  
Apple Payに対応しているものの、まだ設定が済んでいないデバイスに対しては、「Apple Payを設定」ボタンを使って、Apple Payが利用できることを伝えると共に設定の機会を明示的に提供します。

![「Apple Payを設定」ボタン](https://docs-assets.developer.apple.com/published/00631eb03708fc4b58a5be8428a98c10/button-set-up%402x.png)

「Apple Payを設定」ボタンは、設定ページ、ユーザプロフィール画面、インタースティシャルページなどに表示できます。このいずれかの場所でタップされたときに、カードを追加するプロセスが始まるようにする必要があります。

### [ボタンのスタイル](/jp/design/human-interface-guidelines/apple-pay#Button-styles)

 _自動_ スタイルを使用すると、現在のシステムの見た目に応じて、アプリ内のApple Payボタンの見た目が変わります（デベロッパ向けのガイダンスは、[`PKPaymentButtonStyle.automatic`](/documentation/PassKit/PKPaymentButtonStyle/automatic)を参照してください）。自分でボタンの見た目を制御したい場合は、以下のいずれかのオプションを使用できます。Webデベロッパ向けのガイダンスは、[`ApplePayButtonStyle`](/documentation/ApplePayontheWeb/ApplePayButtonStyle)を参照してください。

#### [黒](/jp/design/human-interface-guidelines/apple-pay#Black)

十分なコントラストを確保できる白または明るい色の背景で使用します。黒または暗い背景では使用しないでください。

![黒いApple Payボタンが明るい色の背景に正しく配置されていることを示す図。](https://docs-assets.developer.apple.com/published/710c54f4e84c9e3a4e76df0829642448/apple-pay-black-yes%402x.png)

![正しい使用法](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![黒いApple Payボタンが暗い色の背景に誤って配置されていることを示す図。](https://docs-assets.developer.apple.com/published/90b9135eadb6da6254912c65bca718d0/apple-pay-black-no%402x.png)

![正しくない使用法](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

#### [白（輪郭線あり）](/jp/design/human-interface-guidelines/apple-pay#White-with-outline)

十分なコントラストを確保できない白または明るい色の背景で使用します。暗い背景や濃い色の背景には配置しないでください。

![白いApple Payボタン（輪郭線あり）が明るい色の背景に正しく配置されていることを示す図。](https://docs-assets.developer.apple.com/published/8e6eea702353f528c89d111bb9de2574/apple-pay-outline-yes%402x.png)

![正しい使用法](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![白いApple Payボタン（輪郭線あり）が暗い色の背景に誤って配置されていることを示す図。](https://docs-assets.developer.apple.com/published/48d88126cda8d85659daba16cfddeee5/apple-pay-outline-no%402x.png)

![正しくない使用法](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

#### [白](/jp/design/human-interface-guidelines/apple-pay#White)

十分なコントラストを確保できる暗い色の背景で使用します。

![白いApple Payボタンが暗い色の背景に正しく配置されていることを示す図。](https://docs-assets.developer.apple.com/published/4e1764026fe6451e43d5d9de0fce98ec/apple-pay-white-yes%402x.png)

![正しい使用法](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![白いApple Payボタンが明るい色の背景に誤って配置されていることを示した図。](https://docs-assets.developer.apple.com/published/1939bf3b85837f38601c9d454d95de40/apple-pay-white-no%402x.png)

![正しくない使用法](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

### [ボタンのサイズと位置](/jp/design/human-interface-guidelines/apple-pay#Button-size-and-position)

**Apple Payボタンを目立たせる。** Apple Payボタンはほかの支払いボタンよりも小さくせず、スクロールしなくても見える位置に配置します。

![カスタムの「カートに追加」ボタンの上に正しく配置されたApple Payボタンを示す図。両方のボタンが同じサイズになっています。](https://docs-assets.developer.apple.com/published/7d8f14472f7c19a7122df57e3a0adb2c/ap-same-size-correct%402x.png)

![正しい使用法](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![Apple Payボタンが誤って小さくなっていることを示す図。その下にあるカスタムの「カートに追加」ボタンの方が大きくなってしまっています。](https://docs-assets.developer.apple.com/published/6d97fcc0ec30fecc4ce35a8a558b52fd/ap-smaller-incorrect%402x.png)

![正しくない使用法](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

**Apple Payボタンと「カートに追加」ボタンを正しい位置関係で配置する。** 横に並べるレイアウトでは、Apple Payボタンは「カートに追加」ボタンの右に配置します。

![配置が正しいことを示す図。「Apple Payで購入に進む」ボタンがカスタムの「カートに追加」ボタンの右にあります。](https://docs-assets.developer.apple.com/published/690dd2d6003ab5c8bf6eb16d18a986d3/ap-right-side-correct%402x.png)

![正しい使用法](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![配置が正しくないことを示す図。「Apple Payで購入に進む」ボタンがカスタムの「カートに追加」ボタンの左に来てしまっています。](https://docs-assets.developer.apple.com/published/3a99fdf76ae90d2acb408b4f5794673b/ap-left-side-incorrect%402x.png)

![正しくない使用法](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

縦に並べるレイアウトでは、Apple Payボタンは「カートに追加」ボタンの上に配置します。

![配置が正しいことを示す図。「Apple Payで購入に進む」ボタンがカスタムの「カートに追加」ボタンの上にあります。](https://docs-assets.developer.apple.com/published/7d8f14472f7c19a7122df57e3a0adb2c/ap-top-correct%402x.png)

![正しい使用法](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![配置が正しくないことを示す図。「Apple Payで購入に進む」ボタンがカスタムの「カートに追加」ボタンの下に来てしまっています。](https://docs-assets.developer.apple.com/published/fd01b71d7704b912bd013e1e026a8ba6/ap-below-incorrect%402x.png)

![正しくない使用法](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

**ほかのボタンの見た目と一致するように角丸半径を調整する。** デフォルトでは、Apple Payボタンの角は丸くなっています。角丸半径を変更して、角を直角にしたり、カプセル型のボタンにしたりすることができます。デベロッパ向けのガイダンスは、[`cornerRadius`](/documentation/PassKit/PKPaymentButton/cornerRadius)を参照してください。

![「Apple Payで購入に進む」ボタンがカスタムの「カートに追加」ボタンの上に表示されている図。どちらのボタンも角が直角になっています。](https://docs-assets.developer.apple.com/published/1f511328e20d5ffe6253318ebb309c93/minimum-corner-radii%402x.png)最小の角丸半径

![「Apple Payで購入に進む」ボタンがカスタムの「カートに追加」ボタンの上に表示されている図。どちらのボタンもデフォルトの角丸半径を使用しています。](https://docs-assets.developer.apple.com/published/2b1e437cf6df7e5a807cf255571e4d64/default-corner-radii%402x.png)デフォルトの角丸半径

![「Apple Payで購入に進む」ボタンがカスタムの「カートに追加」ボタンの上に表示されている図。どちらのボタンも最大の角丸半径を使用しており、見た目が長円形になっています。](https://docs-assets.developer.apple.com/published/85e1697ec7f6e0483070d372640326ae/maximum-corner-radii%402x.png)最大の角丸半径

**最小ボタンサイズとボタン周りの最小マージンを維持する。** ロケールによってボタンタイトルの長さが変わる場合があることに注意してください。

注意

使用している支払いボタンの翻訳後のタイトルがボタンの指定サイズに収まらない場合は、自動的に下図の左側のシンプルなApple Payボタンに置き換わります。「Apple Payを設定」ボタンでは、この自動置換は行われません。

![Apple Payボタンの図。最小マージンがボタンの高さの1/10、最小幅が100ポイント、最小高さが30ポイントであることがラベルで示されています。](https://docs-assets.developer.apple.com/published/05c68bd342feb812e24875982fba4760/minimum-apple-pay%402x.png)

![「Apple Payで寄付」ボタンの図。最小マージンがボタンの高さの1/10、最小幅が140ポイント、最小高さが30ポイントであることがラベルで示されています。](https://docs-assets.developer.apple.com/published/4b6dc0c7d049ad13028386d9622c5017/minimum-apple-pay-donate%402x.png)

以下の値を参考にしてください。

ボタン| 最小幅| 最小高さ| 最小マージン  
---|---|---|---  
Apple Pay| 100pt（100px @1x、200px @2x）| 30pt（30px @1x、60px @2x）| ボタンの高さの1/10  
Apple Payで予約| 140pt（140px @1x、280px @2x）| 30pt（30px @1x、60px @2x）| ボタンの高さの1/10  
Apple Payで購入  
Apple Payで購入に進む  
Apple Payで寄付  
Apple Payを設定  
Apple Payでサブスクリプション  
  
### [Apple Payマーク](/jp/design/human-interface-guidelines/apple-pay#Apple-Pay-mark)

ほかの支払いオプションもグラフィックスで表示する場合、利用可能な支払いオプションにApple Payが含まれることを示すにはApple Payマークを使用します。Apple Payマークはボタンではありません。Apple Payボタンが必要な場合は、[ボタンのタイプ](/jp/design/human-interface-guidelines/apple-pay#Button-types)に記載されているいずれかのボタンを使用します。Apple Payを支払いオプションとして表示することに関するデザインのガイダンスは、[Apple Payの提供](/jp/design/human-interface-guidelines/apple-pay#Offering-Apple-Pay)を参照してください。

![4つのクレジットカードのロゴが横一列に並んでいます。すべて同じサイズと形状になっています。一番左のロゴがApple Payマークです。](https://docs-assets.developer.apple.com/published/eb623bea0d2c8176ba590efef4493b9d/apple-pay-mark-with-payment-options%402x.png)

**Appleが提供するアートワークのみを使用し、高さ以外は変更しない。** Apple Payマークの高さは指定できますが、支払いフローに表示されるほかの支払いブランドのマークと同じ高さかそれ以上の高さにしてください。アートワークの幅、角丸半径、アスペクト比を調整してはいけません。商標記号などのコンテンツを追加したり、境界線を削除したり、マークにシャドウやグローや反射などの視覚効果を追加したりしてはいけません。また、Apple Payマークを反転、回転、アニメーションさせてはいけません。

**マークの周りに高さの1/10以上の空白領域を確保する。** Apple Payマークの周囲の境界線を別のグラフィックスやボタンの境界線と重ねてはいけません。

Apple Payマークのグラフィックスのダウンロードと使用ガイドライン全文は、[こちら](/apple-pay/marketing/)を参照してください。

## [Apple Payの言及方法](/jp/design/human-interface-guidelines/apple-pay#Referring-to-Apple-Pay)

すべてのApple製品名と同様、Apple Payは厳密に[Apple商標リスト](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html)に記載されている通りに表記してください。複数形や所有格にしてはいけません。また、[Apple商標および著作権使用に関するガイドライン](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)を順守します。

標準テキストを使用して、Apple Payを推奨したり、Apple Payが支払いオプションであることを示したりすることができます。

**Apple商標リストに記載されているように、テキストではApple Payの語頭は大文字にする。** 2単語の形で _A_ と _P_ を大文字にし、ほかの文字はすべて小文字にします。Apple Payをすべて大文字で表記してよいのは、インターフェイスの所定の表記方法に合わせる必要がある場合のみです（例: テキストをすべて大文字化しているアプリ）。

**テキスト内の _「Apple」_ という名前をAppleロゴで代用しない。**米国では、本文中でのApple Payの初出時には登録商標記号（®）を付けます。会計時にApple Payが選択肢として表示されるときには、登録商標記号は付けません。

| テキストの例  
---|---  
![正しい使用法](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| Apple Payで購入  
![正しい使用法](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| Apple Pay®で購入  
![正しくない使用法](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)| ApplePayで購入  
![正しくない使用法](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)|  Payで購入  
![正しくない使用法](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)| APPLE PAYで購入  
  
**フォントフェイスやフォントサイズをアプリと合わせる。** Appleのタイポグラフィを真似せずに、テキスト属性をアプリやWebサイトのほかの部分と揃えてください。

** _Apple Pay_ やその他のAppleの商標を翻訳しない。**英語以外の言語で使用する場合であっても、Appleの商標は常に英語で使用します。

**支払い選択のコンテキストでは、すべての支払いオプションがテキストのみで説明されている場合に限り、Apple Payをテキストのみで説明してよい。** ほかの支払いオプションの説明にアイコンやロゴが含まれている場合は、[Apple Payの提供](/jp/design/human-interface-guidelines/apple-pay#Offering-Apple-Pay)の説明に従ってApple Payマークを使用する必要があります。

**アプリでApple Payの使用を推奨する場合はApp Storeガイドラインに従う。** アプリでApple Payを推奨する前に、[App Storeマーケティングガイドライン](https://developer.apple.com/app-store/marketing/guidelines/)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/apple-pay#Platform-considerations)

 _iOS、iPadOS、macOS、visionOS、watchOSに追加の考慮事項はありません。tvOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/apple-pay#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/apple-pay#Related)

[Apple Payマーケティングガイドライン](https://developer.apple.com/apple-pay/marketing/)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/apple-pay#Developer-documentation)

[Apple Pay](/documentation/PassKit/apple-pay) — PassKit

[Apple Pay on the Web](/documentation/ApplePayontheWeb)

[`WKInterfacePaymentButton`](/documentation/WatchKit/WKInterfacePaymentButton) — WatchKit

#### [ビデオ](/jp/design/human-interface-guidelines/apple-pay#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/201)

## [変更履歴](/jp/design/human-interface-guidelines/apple-pay#Change-log)

日付| 変更内容  
---|---  
2024年6月10日| WebでのApple Payの提供に関するデベロッパ向けのガイダンスのリンクを更新。  
2023年9月12日| アートワークをアップデート。  
2023年5月02日| ガイダンスを1ページに統合しました。
