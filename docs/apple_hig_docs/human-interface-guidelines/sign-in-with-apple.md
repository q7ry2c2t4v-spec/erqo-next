# Appleでサインイン

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/sign-in-with-apple

# Appleでサインイン

「Appleでサインイン」は、プライバシーを保護しながらアプリやWebサイトに素早くサインインできる機能です。この機能に対応していれば、ユーザは信頼できる方法によって首尾一貫した体験を得ることができ、アカウント名やパスワードをいくつも覚えておく必要もなくなります。

![Appleロゴのスケッチ。「Appleでサインイン」を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる青色になっています。](https://docs-assets.developer.apple.com/published/d61b7d4719dae403705504778ba078d3/technologies-SIWA-intro%402x.png)

「Appleでサインイン」に対応しているアプリやWebサイトでは、ユーザは自分のApple Accountでサインインや登録ができます。フォームへの入力も、メールアドレスの認証も、パスワードの設定も必要ありません。名前やメールアドレスの入力を求められた場合でも、個人のメールアドレスに自動的にメッセージをリレー転送する一意のランダムなメールアドレスを共有することを選択できます。デベロッパ向けのガイダンスは、[Authentication Services](/documentation/AuthenticationServices)を参照してください。

「Appleでサインイン」は、Apple以外のプラットフォームを含め、あらゆるプラットフォームのあらゆるバージョンのアプリまたはWebサイトに実装できます。

「Appleでサインイン」では、Face ID、Touch ID、Optic IDでの認証が簡単になるほか、ビルトインの2ファクタ認証によってセキュリティを強化できます。Appleは、「Appleでサインイン」を使ってアプリ内のユーザやアクティビティをプロファイリングすることはありません。

## [「Appleでサインイン」の提供](/jp/design/human-interface-guidelines/sign-in-with-apple#Offering-Sign-in-with-Apple)

ユーザの利便性を最大限に考えて「Appleでサインイン」を提供する方法については、以下のガイドラインに従ってください。

**価値を提供できる場合にのみユーザにサインインを求める。** ユーザはなぜサインインを求められているのか知る必要があるので、サインインのメリットを簡潔に分かりやすく説明すると効果的な場合があります。例えば、アプリ体験のパーソナライズや追加機能の利用、データの同期といった、サインインのメリットを伝えることをおすすめします。

**サインインはできる限りあと回しにする。** まだ特に何もしていない段階でサインインを求められると、多くのユーザは離脱してしまいます。アプリを少し使う時間を与えてから、サインインを求めるようにしましょう。例えばライブストリーミングアプリなら、視聴可能なコンテンツを一通り見てもらってから、ストリーミングに必要なサインインを求めます。

**アプリの使用にアカウントが必要な場合は、アカウントの設定後にサインインオプションを提示する。** まずは、アカウントが必要な理由を説明しましょう。そして、アカウントの設定完了後に、「Appleでサインイン」やその他の対応しているサインインオプションを提示して、都合のよいサインインオプションをユーザに選んでもらいます。

**既存アカウントを「Appleでサインイン」にリンクできるようにすることを検討する。** このリンク設定に対応していれば、設定済みアカウントの情報へのアクセスを維持しながら「Appleでサインイン」を使えるようになるので便利です。アカウントのリンク設定を提案するのは、既存アカウントへのサインインの前後どちらでもかまいません。例えば以下のような設計が考えられます。

  * 「Appleでサインイン」で共有されたメールアドレスと一致するメールアドレスが既存アカウントの中にあった場合に、「Appleでサインイン」とそのアカウントをリンクすることを提案する。

  * 既存のユーザ名とパスワードを使ってサインインしたユーザに対し、アカウント設定画面などの合理的な場所でアカウントのリンクを提案する。

**コマースアプリの場合は購入完了後にアカウントの作成を求める。** ゲストチェックアウトに対応している場合は、チェックアウト完了後にアカウントを素早く作成できる手段を提供しましょう。例えば、Apple Payに対応している場合は、注文確認ページでアカウントを作成できるようにします。Apple Payでの取引時に名前とメールアドレスの入力が済んでいる場合、その情報を求める必要はありません。

![iPhoneの注文確認画面の図。「アカウントを作成」ボタンと「Appleでサインアップ」ボタンがあります。](https://docs-assets.developer.apple.com/published/a08fc98c7fa7f153400833968396ec5e/create-account-after-purchase%402x.png)

**「Appleでサインイン」の完了後すぐに新規アカウントを利用できるようにする。** 必須ではない情報の入力を求めて体験の提供を遅らせるのではなく、すぐに新規アカウントを利用できるようにしましょう。

**サインイン中であることが分かるようにする。** 設定画面やアカウント画面に「Appleでサインインを使用中」などの文言を表示して、サインインに使っている手段が分かるようにしましょう。

## [データの収集](/jp/design/human-interface-guidelines/sign-in-with-apple#Collecting-data)

ユーザにとっての「Appleでサインイン」のメリットは、プライバシーの保護と利便性です。アプリやWebサイトで生年月日や居住地域などの追加情報が必要になる場合もありますが、アカウント設定時にリクエストするデータは最小限にとどめることが重要です。「Appleでサインイン」に対するユーザの信頼を保てるように、追加でデータが必要な場合はその理由を説明し、受け取ったデータをはっきりと表示するようにしてください。

**リクエストした追加情報の入力が必須なのか推奨なのかを明示する。** 利用規約への同意や、居住地域/居住国、生年月日、または地域の実名登録関連の法律で求められる情報など、法律上または契約上の理由でそのデータが必要な場合は、アカウントの設定に際してその追加情報の入力が必須であることが分かるようにしてください。追加情報は必須ではないがユーザ体験の向上に役立つ場合は、入力が任意であることを伝え、情報を提供することのメリットを説明するようにします。

**ユーザにパスワードの設定を求めない。** 「Appleでサインイン」の大きなメリットは、新たなパスワードを作成して覚えておく必要がない点にあります。ユーザがあなたのアプリやWebサイトで「Appleでサインイン」の使用をやめた場合を除き、パスワードは求めないでください。

**プライバシーを保護するためにプライベートリレーアドレスを提供することにしたユーザには、個人のメールアドレスを尋ねない。** 「Appleでサインイン」では、ユーザがプライバシーを保護するために、個人の認証済みメールアドレスにメッセージを自動転送するプライベートリレーアドレスの共有を選択することがあります。この選択を尊重することは非常に重要です。個人のメールアドレスを尋ねることによってその選択がなかったことにならないようにしてください。カスタマーサービスや商品の販売など、メールアドレスでの認証を求める体験を提供する場合は、以下のような方法を採ることができます:

  * ユーザがアプリまたはWebサイトでプライベートのプライベートリレーアドレスを表示できるようにする

  * 「設定」＞「Apple Account」＞「パスワードとセキュリティ」＞「Apple Accountを使用中のアプリ」に誘導してプライベートリレーアドレスを取得してもらう

  * 注文番号や購入時に取得した電話番号など、その他の識別情報を使用する

**任意のデータを求めるのはアプリを使ってもらってからにする。** 追加情報の提供によってメリットを得られるような場所を、アプリを使うユーザが見つけられるようにしましょう。例えば、連絡先の電話番号を入力すれば最新情報をSMSでリアルタイムに受け取れる、SNSの情報を入力すると友達とゲームをプレイできる、といった提案をしてみます。ユーザが任意の情報を提供しない場合でも、アカウントにアクセスできないようにしたり、アプリで利用できる機能を制限したりしないでください。

**収集したデータについて透明性を確保する。** 提供したデータがどのように使われるのか分かるアプリやWebサイトはユーザから高く評価されます。透明性を確保するには、例えばユーザが入力した名前やメールアドレスをウェルカムメッセージで使用します。こうすれば、情報の使われ方がはっきりと分かるほか、リレーメールアドレスの確認方法を示すこともできます。提供した情報の中にどこにも表示されないものがあると、なぜ入力を求められたのだろうとユーザに不審がられる可能性があります。

## [ボタンの表示](/jp/design/human-interface-guidelines/sign-in-with-apple#Displaying-buttons)

Appleでは、ユーザにアカウント設定やサインインを求める場面で使える「Appleでサインイン」ボタンをいくつか用意しています。必要な場合は、カスタムの「Appleでサインイン」ボタンを作成することもできます。ガイダンスは[カスタムの「Appleでサインイン」ボタンを作成する場合](/jp/design/human-interface-guidelines/sign-in-with-apple#Creating-a-custom-Sign-in-with-Apple-button)を参照してください。

**「Appleでサインイン」ボタンは見つけやすい場所に置く。** 「Appleでサインイン」ボタンは、ほかのサインインボタンよりも小さくせず、スクロールしなくても見える位置に配置します。

### [システムで提供されているボタンを使う場合](/jp/design/human-interface-guidelines/sign-in-with-apple#Using-the-system-provided-buttons)

システムで提供されているAPIを使って「Appleでサインイン」ボタンを作成する場合は、以下のようなメリットがあります。

  * Appleによって承認されている見た目を確実に使用できる

  * スタイルを変更してもボタンのコンテンツの理想的な比率が保たれる

  * ボタンのタイトルが、デバイスで設定されている言語のものに自動的に切り替わる

  * ボタンの角丸半径をUIのスタイルと一致するように設定できる（iOS、macOS、Web）

  * VoiceOverで読み上げることができる代替テキストラベルがシステムによって提供される

デベロッパ向けのガイダンスは、[`ASAuthorizationAppleIDButton`](/documentation/AuthenticationServices/ASAuthorizationAppleIDButton)（iOS、macOS、tvOSの場合）、[`WKInterfaceAuthorizationAppleIDButton`](/documentation/WatchKit/WKInterfaceAuthorizationAppleIDButton)（watchOSの場合）、および[Webでの「Appleでサインイン」ボタンの表示](/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web)を参照してください。また、[「Appleでサインイン」ボタン](https://appleid.apple.com/signinwithapple/button)では、Webベースボタンのライブプレビューの表示と調整が可能なほか、コードを取得することができます。

システムでは、複数のバリエーションのボタンタイトルが用意されています。コンテンツを提供するプラットフォームに応じて、サインイン画面の文言に合ったバリエーションを選択し、インターフェイス全体で同じものを使用してください。

iOS、macOS、tvOS、Webでは、以下のボタンタイトルを使用できます。

![Appleロゴと「Appleでサインイン」というテキストを含むボタンの図。](https://docs-assets.developer.apple.com/published/7510291ce4d0cd5b91bd325078a054e9/apple-account-sign-in-with%402x.png)

![Appleロゴと「Appleでサインアップ」というテキストを含むボタンの図。](https://docs-assets.developer.apple.com/published/388906b461513478bbce1fe4cc630580/apple-account-sign-up-with%402x.png)

![Appleロゴと「Appleで続ける」というテキストを含むボタンの図。](https://docs-assets.developer.apple.com/published/79964d884643f563e51cfbc5df0853b0/apple-account-continue-with%402x.png)

watchOSには、「 サインイン」という1つのボタンタイトルのみ提供されています。

![watchOS向けのボタンの図。Appleロゴと「サインイン」というテキストが含まれています。](https://docs-assets.developer.apple.com/published/3a70b1f9a818c85bcc92761c26c6ae56/apple-account-watch-44mm-no-background%402x.png)

プラットフォームに応じて、「Appleでサインイン」ボタンの見た目は最大で3つの選択肢（白、白（輪郭線あり）、黒）の中から選ぶことができます。ボタンが表示される画面の背景に最も適した見た目を選んでください。

#### [白](/jp/design/human-interface-guidelines/sign-in-with-apple#White)

白のスタイルは、すべてのプラットフォームおよびWebで使用できます。背景が暗い色で、十分なコントラストを確保できる場合に使用します。

![白いボタンの正しい使い方を示した図。暗い色の背景の上に配置されています。ボタンにはAppleロゴと「Appleでサインイン」というテキストが含まれています。](https://docs-assets.developer.apple.com/published/52f84df8a5d3921114072cafe76d1cd3/apple-account-white-yes%402x.png)

![丸に囲まれたチェックマークは正しい使い方を示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![白いボタンの正しくない使い方を示した図。明るい色の背景の上に配置されています。ボタンにはAppleロゴと「Appleでサインイン」というテキストが含まれています。](https://docs-assets.developer.apple.com/published/c3c4e3ed3533fbc8864352c6da51f542/apple-account-white-no%402x.png)

![丸に囲まれた×印は不適切な使い方を示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

#### [白（輪郭線あり）](/jp/design/human-interface-guidelines/sign-in-with-apple#White-with-outline)

白（輪郭線あり）のスタイルは、iOS、macOS、およびWebで使用できます。背景が白または明るい色で、白で塗りつぶされたボタンでは十分なコントラストを確保できない場合に使用します。背景が暗い色や濃い色の場合は黒い輪郭線によって見た目がうるさくなることがあるので、このスタイルではなく、[白](https://developer.apple.com/jp/design/human-interface-guidelines/sign-in-with-apple#White)のスタイルを使用して暗い背景とのコントラストを確保してください。

![白（輪郭線あり）ボタンの正しい使い方を示した図。明るい色の背景の上に配置されています。ボタンにはAppleロゴと「Appleでサインイン」というテキストが含まれています。](https://docs-assets.developer.apple.com/published/b47cf86de6868de43b8d7503337522fe/apple-account-outline-yes%402x.png)

![丸に囲まれたチェックマークは正しい使い方を示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![白（輪郭線あり）ボタンの正しくない使い方を示した図。暗い色の背景の上に配置されています。ボタンにはAppleロゴと「Appleでサインイン」というテキストが含まれています。](https://docs-assets.developer.apple.com/published/6268116e2d5a47d1fc06a359de891181/apple-account-outline-no%402x.png)

![丸に囲まれた×印は不適切な使い方を示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

#### [黒](/jp/design/human-interface-guidelines/sign-in-with-apple#Black)

黒のスタイルは、すべてのプラットフォームおよびWebで使用できます。背景が白または明るい色で、十分なコントラストを確保できる場合に使用します。背景が黒または暗い色の場合は使用しないでください。

![黒いボタンの正しい使い方を示した図。明るい色の背景の上に配置されています。ボタンにはAppleロゴと「Appleでサインイン」というテキストが含まれています。](https://docs-assets.developer.apple.com/published/915b5d4767463bca63ab0adafa6846f9/apple-account-black-yes%402x.png)

![丸に囲まれたチェックマークは正しい使い方を示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![黒いボタンの正しくない使い方を示した図。暗い色の背景の上に配置されています。ボタンにはAppleロゴと「Appleでサインイン」というテキストが含まれています。](https://docs-assets.developer.apple.com/published/c3da65d8c76a981f91ebfdaf21de74af/apple-account-black-no%402x.png)

![丸に囲まれた×印は不適切な使い方を示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

ほかのプラットフォーム用の黒い「Appleでサインイン」ボタンとは異なり、watchOS用のボタンでは、真っ黒ではない塗りつぶしカラーが使用されます。Apple Watchの真っ黒な背景とコントラストが出るように、システムで定義されている濃いグレイの見た目が使用されます。

![watchOS向けの黒い色のボタンの図。Appleロゴと「サインイン」というテキストを含むボタンが、暗い背景の上に配置されています。](https://docs-assets.developer.apple.com/published/dbd9944a0b54c61b4ad31ae7a1ba5a82/apple-account-watch-44mm%402x.png)

#### [ボタンのサイズと角丸半径](/jp/design/human-interface-guidelines/sign-in-with-apple#Button-size-and-corner-radius)

**アプリ内のほかのボタンと見た目が揃うように角丸半径を調整する。** デフォルトでは、「Appleでサインイン」ボタンの角は丸くなっています。iOS、macOS、Webの場合は、角丸半径を変更して、角を直角にしたり、カプセル型のボタンにしたりすることができます。デベロッパ向けのガイダンスは、[`cornerRadius`](/documentation/AuthenticationServices/ASAuthorizationAppleIDButton/cornerRadius)（iOS、macOSの場合）および[Webでの「Appleでサインイン」ボタンの表示](/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web)を参照してください。

![角が直角になっている「Appleでサインイン」ボタンの図。](https://docs-assets.developer.apple.com/published/4f279ff515dfcb50faf6f085acceffb9/apple-account-minimum-corner-radii%402x.png)最小の角丸半径

![デフォルトの角丸半径が使用されている「Appleでサインイン」ボタンの図。](https://docs-assets.developer.apple.com/published/7510291ce4d0cd5b91bd325078a054e9/apple-account-default-corner-radii%402x.png)デフォルトの角丸半径

![最大の角丸半径が使用されている「Appleでサインイン」ボタンの図。カプセルのような見た目になっています。](https://docs-assets.developer.apple.com/published/baeeaf354ab05437b35812f154e33497/apple-account-maximum-corner-radii%402x.png)最大の角丸半径

**最小ボタンサイズとボタン周りの最小マージンを維持する（iOS、macOS、Webの場合）。** ロケールによってボタンタイトルの長さが変わる場合があることに注意してください。以下の値を参考にしてください。

最小幅| 最小高さ| 最小マージン  
---|---|---  
140pt (140px @1x, 280px @2x)| 30pt (30px @1x, 60px @2x)| ボタンの高さの1/10  
  
### [カスタムの「Appleでサインイン」ボタンを作成する場合](/jp/design/human-interface-guidelines/sign-in-with-apple#Creating-a-custom-Sign-in-with-Apple-button)

インターフェイスで必要な場合は、iOS、macOS、またはWeb向けのカスタムの「Appleでサインイン」ボタンを作成できます。例えば、複数のサインインボタン間でロゴの位置を揃える場合、ロゴのみのボタンを使用する場合、フォント、ベゼル、または背景の見た目を周囲のUIに合うように調整する場合などです。

![サインイン画面が表示された2台のiPhoneの一部分に横に並べた図。左の画面では、次の4つのボタンが縦に並んでいます: 「Appleでサインイン」、「Xでサインイン」、「Yでサインイン」、「Zでサインイン」。「Appleでサインイン」ボタンには、Appleロゴに続いてボタンタイトルが表示されています。「Xでサインイン」ボタンには、塗りつぶされた円に続いてタイトルが表示されています。「Yでサインイン」ボタンには、塗りつぶされた正方形に続いてタイトルが表示されています。「Zでサインイン」ボタンには、塗りつぶされた三角形に続いてタイトルが表示されています。右の画面には「以下の方法でサインイン」という見出しがあり、その下に、グリフを含む正方形のボタンが4つ並んでいます。1つ目の正方形のボタンにはAppleロゴが含まれています。2つ目の正方形のボタンには塗りつぶされた円が含まれています。3つ目の正方形のボタンには塗りつぶされた正方形が含まれています。4つ目の正方形のボタンには塗りつぶされた三角形が含まれています。円、正方形、および三角形の図形は、さまざまなロゴを表しています。](https://docs-assets.developer.apple.com/published/ca67a816baa2f5774a3954cb9c1289bb/custom-sign-in-screens%402x.png)

カスタムボタンは、必ず、「Appleでサインイン」ボタンであることが一目で分かるようなものにしてください。標準的なボタンからあまりにもかけ離れていると、ユーザがアカウント設定やサインインに対して不安を抱く可能性があります。カスタムの「Appleでサインイン」ボタンはすべて、App Reviewの審査対象になります。

[Appleのデザインリソース](https://developer.apple.com/design/resources/)では、ロゴのみ、またはロゴとテキストが付いたカスタムの「Appleでサインイン」ボタンを作成するときに使えるAppleロゴ画像をダウンロードできます。ロゴファイルにはPNG、SVG、PDFの形式があり、両方のタイプのボタンについて黒と白の2つのバージョンが用意されています。ロゴのみの画像の黒と白のバージョンは以下のようなものです（見やすくするために、便宜上、背景を付けています）。

![黒いAppleロゴの図。白い正方形がロゴを囲み、さらにその正方形を濃い色の太い枠線が囲っています。白い正方形は、Appleロゴとその他のインターフェイス要素との間に最低限残す必要がある空白領域を表しています。](https://docs-assets.developer.apple.com/published/c449adb9092caa5c115dfd5ce9b83637/siwa-black-logo-only%402x.png)

![白いAppleロゴの図。黒い正方形がロゴを囲み、さらにその正方形を明るい色の太い枠線が囲っています。黒い正方形は、Appleロゴとその他のインターフェイス要素との間に最低限残す必要がある空白領域を表しています。](https://docs-assets.developer.apple.com/published/5c6ba47f5388dfebfd0fb2a5f506aafa/siwa-white-logo-only%402x.png)

ダウンロード可能なすべてロゴファイルには、ロゴをボタンに配置しやすくするためのパディングが入っています。ロゴのみのロゴファイルには、ボタンに対するロゴの比率を正しく保てるようにするためのパディングが上下左右に入っています。ボタンとテキストが付いたロゴファイルには、ロゴとボタンの比率を正しく保つためのパディングに加え、ロゴとボタン先頭側の間、ロゴとタイトルの間の最小マージンを確保するためのパディングが左右に入っています。

[Appleのデザインリソース](https://developer.apple.com/design/resources/)からダウンロードできるロゴ画像のみを使用し、カスタムのAppleロゴは絶対に作成しないでください。カスタムの「Appleでサインイン」ボタンを作成するときは、ダウンロード可能なロゴファイルの使い方に関する以下のガイドラインに従ってください:

  * ロゴファイルはボタン内にAppleロゴを配置するために使用する。絶対にAppleロゴ自体をボタンとして使用しない。

  * ロゴファイルの高さとボタンの高さを一致させる。

  * ロゴファイルを切り取らない。

  * 上下のパディングを追加しない。

システムで提供されている「Appleでサインイン」ボタンと同じものであることが見て分かるように、以下の属性は変更しないでください。

  * タイトル。「 _Appleでサインイン_ 」、「 _Appleでサインアップ_ 」、または「 _Appleで続ける_ 」のみを使用すること。

  * 全体的な形状。ロゴとテキストを組み合わせたボタンは常に長方形にすること。ロゴのみのボタンは長方形のほかに円形も可。

  * ロゴとタイトルのカラー。ボタン内のこの2つはどちらも必ず黒または白にすること。カスタムカラーは使用しない。

アプリのデザインに合わせる目的で以下のような変更を加えるのはかまいません:

  * タイトルのフォント。フォントの太さとサイズも調整可。

  * タイトルの大文字/小文字の使用。タイトルのすべての文字を大文字化するのも可。

  * 背景の見た目。全体的なカラーは黒または白にすること。ボタンがインターフェイスに調和するように、適宜、微妙な質感やグラデーションを付けるのは可。

  * ボタンの角丸半径。UIのほかのボタンと同じ角丸半径を使用可。

  * ボタンのベゼルとシャドウ。例えば、線を使ってボタンのベゼルを強調したり、ドロップシャドウを追加したりするのは可。

#### [ロゴとテキストを含むカスタムボタン](/jp/design/human-interface-guidelines/sign-in-with-apple#Custom-buttons-with-a-logo-and-text)

**ボタンの高さを考えてロゴファイルの形式を選ぶ。** SVGとPDFはベクター形式なので、どのような高さのボタンでも使用できます。PNGは、高さがiOSのデフォルトのボタン高さ（推奨値）である44ポイントのボタンでのみ使用してください。ロゴには大中小のサイズがあるので、表示するすべての登録ボタンのロゴサイズを揃えることができます。

**タイトル（「Appleでサインイン」、「Appleでサインアップ」、「Appleで続ける」）はシステムフォントの使用を検討する。** 選んだフォントにかかわらず、カスタムボタンのタイトルとボタン高さは、システム標準のものと同じ比率にしてください。例えばシステムフォントを使う場合は、タイトルのフォントサイズはボタン高さの43%にしてください。つまり、ボタン高さはタイトルのフォントサイズの233%（小数点以下切り上げ）にする必要があります。以下の2つの例では、それぞれシステムフォントのサイズは異なりますが、この比率が保たれています。

![黒い「Appleでサインイン」ボタンの図。ボタン高さが44ポイントで、フォントサイズが19ポイントであることを示すコールアウトが付いています。](https://docs-assets.developer.apple.com/published/7fa868b7473176e995231b309116b5a0/left-aligned-correct-proportions-2%402x.png)

![黒い「Appleでサインイン」ボタンの図。ボタン高さが56ポイントで、フォントサイズが24ポイントであることを示すコールアウトが付いています。](https://docs-assets.developer.apple.com/published/ee2d77b09aa1e609025248723d4ce239/left-aligned-correct-proportions-1%402x.png)

**基本的にタイトルの大文字化のスタイルは変えない。** デフォルトでは、ボタンのどのバリエーションでも最初の単語（ _Sign_ 、 _Continue_ 、 _Apple_ ）の先頭の文字のみ大文字で、ほかの文字は小文字で表記されています。インターフェイスですべてを大文字化している場合を除き、このスタイルは変えないでください。

**ボタン内でのタイトルとロゴの縦方向の位置を揃える。** これを行うには、タイトルをボタンの上下の中央に揃えてから、ボタンと同じ高さのロゴ画像を追加します。ロゴ画像の上下にはパディングが入っているので、タイトルをボタンの上下の中央に揃えれば、タイトル、ロゴ、ボタンの位置を正しく揃えることができます。

**必要に応じてロゴの位置を調整する。** Appleロゴとその他の認証ロゴの横方向の位置を揃える必要がある場合は、Appleロゴとボタン先頭側のスペースを調整します。

**タイトルとボタン右端の最小マージンを維持する。** このマージンは、ボタンの幅の8%以上にしてください。

**最小ボタンサイズとボタン周りの最小マージンを維持する。** ロケールによってボタンタイトルの長さが変わる場合があることに注意してください。以下の値を参考にしてください。

最小幅| 最小高さ| 最小マージン  
---|---|---  
140 pt (140 px @1x, 280 px @2x)| 30 pt (30 px @1x, 60 px @2x)| ボタンの高さの1/10  
  
#### [ロゴのみのカスタムボタン](/jp/design/human-interface-guidelines/sign-in-with-apple#Custom-logo-only-buttons)

**ボタンのサイズを考えてロゴファイルの形式を選ぶ。** ロゴのみのボタンのダウンロード可能な画像には、SVG、PDF、およびPNGの形式があります。ベクター形式であるSVGとPDFはどのようなサイズのボタンでも使用できますが、PNG形式は44x44 ptのボタンでのみ使用してください。

**ロゴのみの画像に左右のパディングを追加しない。** ロゴのみの「Appleでサインイン」ボタンは常に1:1のアスペクト比で使用します。画像には、すでに上下左右に適切なパディングが入っています。

**ロゴのみの画像のデフォルト形状（正方形）を変える場合はマスクを使用する。** 例えば、すべてのサインインボタンをロゴのみにする場合に円形や角丸四角形のマスクを使うなどです。絶対に、Appleが提供している画像を切り取って適用済みのパディングを減らしたり、ロゴ自体を使用したりしないでください。パディングを追加することも避けてください。

![ロゴのみの「Appleでサインイン」ボタンの図。ボタンにはAppleロゴのみが含まれ、ボタンは角丸四角形になっています。](https://docs-assets.developer.apple.com/published/f5e783edee3a2ab6c5171f121e0e1894/siwa-logo-masked-rounded-rect%402x.png)角丸四角形のマスク

![ロゴのみの「Appleでサインイン」ボタンの図。ボタンにはAppleロゴのみが含まれ、ボタンは正方形になっています。](https://docs-assets.developer.apple.com/published/7e4610f57c6a5aca09a64dde7756d7b7/siwa-logo-default%402x.png)マスクなし

![ロゴのみの「Appleでサインイン」ボタンの図。ボタンにはAppleロゴのみが含まれ、ボタンは円形になっています。](https://docs-assets.developer.apple.com/published/ec7ae1718620f0629595ac57950ef561/siwa-logo-masked-circle%402x.png)円形のマスク

**ボタン周りの最小マージンを維持する。** このマージンは、ボタンの高さの1/10以上にしてください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/sign-in-with-apple#Platform-considerations)

 _iOS、iPadOS、macOS、tvOS、visionOS、watchOSに追加の考慮事項はありません。_

## [リソース](/jp/design/human-interface-guidelines/sign-in-with-apple#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/sign-in-with-apple#Related)

[「Appleでサインイン」ボタン](https://appleid.apple.com/signinwithapple/button)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/sign-in-with-apple#Developer-documentation)

[Authentication Services](/documentation/AuthenticationServices)

[Webでの「Appleでサインイン」ボタンの表示](/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web) — Appleでサインイン

#### [ビデオ](/jp/design/human-interface-guidelines/sign-in-with-apple#Videos)

[](https://developer.apple.com/videos/play/wwdc2021/10106)

[](https://developer.apple.com/videos/play/wwdc2021/10279)

[](https://developer.apple.com/videos/play/wwdc2019/706)

## [変更履歴](/jp/design/human-interface-guidelines/sign-in-with-apple#Change-log)

日付| 変更内容  
---|---  
2022年9月14日| 既存のアカウントのサポート、新規アカウントの設定のヘルプ、現在のサインインステータスの表示に関するガイダンスを改訂しました。ガイダンスを1ページに統合しました。
