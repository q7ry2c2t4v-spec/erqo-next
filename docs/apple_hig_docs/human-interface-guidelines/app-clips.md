# App Clip

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/app-clips

# App Clip

App Clipは、アプリやゲームの軽量バージョンで、外出先やデモなどですぐに利用できます。

![点線で囲まれているアプリアイコンのスケッチ。App Clipを示しています。画像の上に長方形と円形のグリッド線が重ねられており、画像全体が6色の初代Appleロゴの青色を連想させる青みを帯びています。](https://docs-assets.developer.apple.com/published/6c6f9a0ff6f715104587d3148140c4f0/technologies-app-clips-intro%402x.png)

App Clipは、App Storeからフルバージョンのアプリをダウンロードすることなく、アプリやゲームを体験できる軽量なアプリです。タスクを迅速に完了することに重点を置いて設計したり、フルバージョンのアプリやゲームを紹介するデモとしても活用できます。App Clipはデバイスに一時的にのみ保存され、ユーザのプライバシーも保護されます。

ユーザがApp Clipを見つけて起動するシチュエーションやコンテキストはさまざまです。物理的な場所では、App Clipコード、NFCタグ、またはQRコードをスキャンしてApp Clipを起動します。ただ、App Clipを見つけて起動してもらうには、たいていはApp Clipコードを使うのがベストでしょう。App Clipコードはデザインが独特なので一目でそれと分かりますし、App Clipを素早く安全に起動できる手段として信頼性があります。

デバイス上では、Siriからの提案で許可した位置情報に基づく検索候補、マップアプリ、Webサイト上のスマートバナー、SafariのApp Clipカードから起動したり、メッセージアプリでほかのユーザから送られたリンクをタップして起動したりします。iOS 17以降では、アプリにリンクとApp Clipプレビューを含め、タップして別のアプリのApp Clipを起動できます。

![iPhoneのロック画面のスクリーンショット。画面の下半分は、あるドーナツショップのApp Clipを呼び出したときに表示されるApp Clipカードです。](https://docs-assets.developer.apple.com/published/daf3581b5210ffac634e2f8689e047c2/app-clips-hero-1%402x.png)

![iPhoneに表示されたドーナツショップのApp Clipのスクリーンショット。ユーザがApp ClipカードでApp Clipの起動を承認すると表示されます。App Clipで注文できるいろいろなドーナツのリストが表示されています。](https://docs-assets.developer.apple.com/published/6f6e9ab2a4ffb24ee7fbc18c7f46ebf4/app-clips-hero-2%402x.png)

一定の時間内に終わるようなタスクを実行するといった瞬間的な体験をアプリで提供している場合は、App Clipの作成を検討してみてください。例えば以下のような使い方ができます:

  * レンタル自転車にApp Clipコードを付け、それをタップまたはスキャンしたときに自転車レンタル用のApp Clipが起動するようにする。

  * カフェのWebサイトにスマートバナーやApp Clipカードを表示し、そこからApp Clipを起動して事前注文できるようにする。Webサイトへのリンクをメッセージアプリで共有できるようにして、それを受け取った人がリンクをタップしてメッセージアプリ内でApp Clipを起動できるようにする。

  * フードトラックの販促素材（季節限定メニューの販促ポスターなど）にApp Clipコードを含め、そのApp Clipコードをデバイスのカメラアプリでスキャンしたときに、季節限定メニューを注文するためのApp Clipが即座に起動するようにする。

  * 飲食店で、マップアプリまたは「Siriからの提案」から起動できるApp Clipや、テーブルにあるApp ClipコードまたはNFCタグにデバイスをかざして起動できるApp Clipから食事代を支払えるようにする。

  * 博物館や美術館で、展示作品の横のラベルにApp ClipコードまたはQRコードをプリントし、それをスキャンして起動できるApp ClipからARコンテンツを体験したり音声解説を聞いたりできるようにする。

購入やサブスクリプションを決定する前に、アプリやゲームを体験できるようにするApp Clipの作成を検討してみてください。アプリやゲームを体験して理解する機会を提供することに重点を置きます。例えば以下のような使い方ができます:

  * ゲームで、チュートリアルと最初のレベルを含むデモバージョンをプレイできるApp Clipを提供する。

  * フィットネスアプリで、無料のワークアウトとガイド付きの瞑想を含むApp Clipを提供する。

  * テキストエディタで、デモのApp Clipを使用して書類を作成し保存できるようにする。

デベロッパ向けのガイダンスは、[App Clips](/documentation/AppClip)を参照してください。

## [App Clipの設計](/jp/design/human-interface-guidelines/app-clips#Designing-your-App-Clip)

**App Clipでタスクやデモを完了できるようにする。** デモをすべて体験したり、タスクを完了したり、ゲームのレベルをクリアしたりするために、フルバージョンのアプリをインストールしてもらう必要はありません。

**必須機能に的を絞る。** 特定の目的に特化したスピーディーな操作がApp Clipの特長です。目の前のタスクを実行するのに必要な機能だけに絞ってください。詳細な機能や複雑な機能はフルバージョンのアプリのみにとどめます。フルバージョンのアプリのデモバージョンを提供する場合は、ゲームやアプリの機能についてユーザに良い印象を与える重要な機能に焦点を当てます。

**マーケティングのみの目的では利用しない。** App Clipでは、中身のあるコンテンツを提供し、タスクの実行をサポートする必要があります。App Clipをサービスや商品を宣伝する手段として使ったり、App Clip内に広告を表示したりしないでください。

**App ClipでWebビューを使用しない。** App Clipは、ネイティブのコンポーネントとフレームワークを使用してアプリと同等の体験を実現するためのものです。Webコンポーネントしか利用できない場合は、App ClipではなくWebサイトへのクイックリンクを提示してください。

**フローが直線的で、使い方が簡単で、特定の目的に特化したユーザインターフェイスにする。** App Clipにタブバー、複雑なナビゲーション、設定は必要ありません。画面や入力フォームの数を最小限にとどめます。無関係な情報を省き、ユーザインターフェイスをできる限りシンプルにしましょう。

**起動時に最も関連のある部分が表示されるようにする。** 不要な手順を飛ばして、App Clipの中でユーザの状況に最も合致する部分に即座に遷移してください。

**App Clipを即座に使えるようにする。** 必要なアセットをすべて含め、スプラッシュスクリーンを省き、起動時にユーザを待たせないようにする必要があります。

**App Clipのサイズは小さくする。** App Clipのサイズが小さいほど、デバイスでの起動が速くなります。帯域幅が限られている状況では、App Clipのサイズを小さくすることが特に重要です。できる限り、不要なコードを減らし、使わないアセットを削除してください。即時性が薄れることがあるので、追加データをダウンロードさせることは避けてください。

**App Clipを共有可能にする。** メッセージアプリでApp Clipのリンクを受け取った場合は、メッセージアプリ内でApp Clipを起動できます。App Clip内の特定の場所へのリンクを共有できるようにして、ユーザにApp Clipを共有するように促しましょう。

**サービスや商品の代金を簡単に支払えるようにする。** 支払い情報の入力は、時間がかかる上に間違いが起こりやすい作業です。エクスプレスチェックアウト機能を提供し、ユーザが配送情報をタイピングなしで入力できるように、[Apple Pay](/jp/design/human-interface-guidelines/apple-pay)に対応することを検討してください。

**App Clipの利用前にユーザにアカウントの作成を要求しない。** アカウントの作成は面倒で手間がかかります。アカウントを必要としない方法を検討するか、タスクの完了後にアカウントの作成を求めることを考えてください。App Clipで価値を提供するのにどうしてもアカウントが必要な場合は、「[Appleでサインイン](/jp/design/human-interface-guidelines/sign-in-with-apple)」を利用できるようにするなどして、ユーザが入力する情報が多くならないようにしてください。

**特定の目的に特化した馴染みのある機能をアプリ本体でも提供する。** デバイスにフルバージョンのアプリがインストールされると、App Clipがそのアプリに置き換わります。以降は、App Clipを起動する操作をするとフルバージョンのアプリが開くようになるので、App Clipを使用していたユーザにとって馴染みのある、特定の目的に特化した機能をフルバージョンのアプリでも提供するようにしてください。フローを妨げるような追加の手順を要求しないようにしてください。例えば、App Clipからアプリ本体へ移行する際に、ユーザにあらためてログインを要求することは避けましょう。

### [プライバシーの保護](/jp/design/human-interface-guidelines/app-clips#Preserving-privacy)

App Clipには、ユーザのプライバシーを保護するための制限が課されます。例えば、App Clipはバックグラウンドで処理を実行できません。デベロッパ向けのガイダンスは、[App Clipに最適な機能の選択](/documentation/AppClip/choosing-the-right-functionality-for-your-app-clip)を参照してください。

**保存して処理するデータの量を制限する。** ユーザのデータ（ログイン情報など）を保存する必要がある場合は、安全な形で保存してください。加えて、デバイスに以前に保存したデータを使えるだろうという前提を持たないでください。App Clipおよびそのすべてのデータは、前回の起動後にシステムによって削除されている可能性があります。ログイン情報を保存するのであれば、デバイス外に安全に保存してください。

**「Appleでサインイン」を利用できるようにする。** 「Appleでサインイン」を利用すると、ログイン情報がユーザのデバイス外で安全に保管され、ユーザのプライバシーも保護されます。ガイダンスは、[Appleでサインイン](/jp/design/human-interface-guidelines/sign-in-with-apple)を参照してください。

**ユーザのプライバシーに配慮しながらサービスや商品の代金を安全に支払える方法を提供する。** 例えば、[Apple Pay](/jp/design/human-interface-guidelines/apple-pay)に対応することを検討します。

### [アプリ本体の紹介](/jp/design/human-interface-guidelines/app-clips#Showcasing-your-app)

App Clipはユーザ自身が管理するものではなく、ホーム画面に表示されることもありません。一定の期間利用されなかったApp Clipはシステムによって自動的に削除されます。

継続的に使用してもらうにはアプリがベストであることに変わりはないため、システムには、フルバージョンのアプリの発見とインストールを促す以下の機能が搭載されています:

  * App Clipカード。App Clipを起動したり、フルバージョンのアプリのApp Storeページを開いたりできます。

  * App Clipの初回起動時に画面上部に表示されるアプリバナー。App Clipカードと同様に、このバナーからもアプリのApp Storeページを開くことができます。

そのほか、App Clipにオーバーレイを表示して、そこからフルバージョンのアプリをダウンロードできるようにすることも可能です。

**フルバージョンのアプリのインストールを求めることでユーザ体験を損なわないようにする。** 外出先での体験を提供するApp Clipの場合、App Clipカードやシステムのアプリバナーから、十分にダウンロードの動機付けができないか考えてみてください。デモ体験を提供するApp Clipの場合、フルバージョンのアプリのインストールを求める前に、ユーザにデモをすべて体験してもらってください。

**アプリを推奨する適切なタイミングを見極める。** ユーザがタスクを完了したときや、自然な休止位置に到達したときは、[`SKOverlay`](/documentation/StoreKit/SKOverlay)を表示して、App Clipのコンテキストからフルバージョンのアプリやゲームのダウンロードを開始できるようにします。

**ユーザの邪魔をせず、節度を守ってアプリを推奨する。** フルバージョンのアプリのインストールを何度もすすめたり、タスクに割り込む形ですすめたりしないでください。プッシュ通知も、アプリのインストールをすすめる方法としては不適切です。フルバージョンのアプリで利用できる追加機能を明確に伝えてください。

デベロッパ向けのガイダンスは、[App Clipに対応するAppの案内](/documentation/AppClip/recommending-your-app-to-app-clip-users)を参照してください。

### [通知の制限](/jp/design/human-interface-guidelines/app-clips#Limiting-notifications)

App Clipには、通知を受け取るタイミングを、起動時点から8時間後までの間で設定できるオプションがあります。ほとんどの一般的なタスクのフォローアップや完了に十分な時間です。

**ユーザに通知の許可を求めるのは、しばらく時間が経ってからの通知が本当に必要な場合にのみにする。** App Clipの機能が1日以上続く場合は、通知のスケジュール設定と受信のための許可を明示的に求めてください。例えば、レンタカー会社のApp Clipであれば、ユーザに車の返却期限が迫っていることを通知するための許可を要求する場合があるかもしれません。

**目的のはっきりした通知だけを送る。** 単なる販促目的の通知を送信しないでください。通知は、ユーザの明示的なアクションがあった場合にのみ使用します。ユーザがApp Clipを起動したあと、ほかのアプリに切り替えずにそのままタスクを完了した場合は、通知を送信する必要は一切ないでしょう。

**タスクの完了に役立つ通知を送信する。** App Clipからの通知は、ユーザがApp Clipで完了しようとしているタスクに直接関連するものにします。例えば、料理のデリバリーを注文できるApp Clipなら、配達予定に関する通知を送信するといった使い方が考えられます。

デベロッパ向けのガイダンスは、[App Clipでの通知の有効化](/documentation/AppClip/enabling-notifications-in-app-clips)を参照してください。

### [ビジネス向けのApp Clipの作成](/jp/design/human-interface-guidelines/app-clips#Creating-App-Clips-for-businesses)

ビジネス向けのプラットフォームプロバイダの場合は、[App Store Connect](https://appstoreconnect.apple.com)で複数のApp Clip体験を作成し、それらすべてを1つのApp Clipで実現することもあるでしょう。App Clipのユーザには、プロバイダのブランドではなく、個々のビジネスや拠点のブランドで表示されるようにしてください。

**一貫したブランディングを行う。** ビジネス向けに作成したApp Clipカードでは、そのビジネスのブランドを前面に押し出します。App Clipを起動したユーザが戸惑わないように、プロバイダ自身のブランディングは抑え、ビジネスのブランドが明確に提示されるようにしてください。

**複数のビジネスが対象であることを考慮に入れる。** 1つのApp Clipをさまざまなビジネスが利用したり、複数の店舗を持つビジネスが利用したりすることが考えられます。どちらの場合でも、ユーザは1つのApp Clipを使って一度に複数のビジネスや店舗を表示することになるかもしれません。提供するApp Clipでは、このようなユースケースにうまく対応し、適宜ユーザインターフェイスをアップデートしてください。例えば、最近使ったビジネスや店舗をApp Clip内で切り替えたり、起動した場所を確認したりできるようにすることを検討してください。

デベロッパ向けのガイダンスは、[App Clip体験の構成](/documentation/AppClip/configuring-the-launch-experience-of-your-app-clip)を参照してください。

## [App Clipカードのコンテンツの作成](/jp/design/human-interface-guidelines/app-clips#Creating-content-for-an-App-Clip-card)

システムが提供するApp Clipカードは、App Clipを起動したユーザが最初に目にするものです。その画像や文言は慎重に検討する必要があります。

**有益な情報を伝える。** App Clipカードの画像で、App Clipが提供する機能、対応するタスク、コンテンツを明確に伝えるようにしてください。

**なるべく写真やグラフィックスを使う。** アプリのユーザインターフェイスのスクリーンショットを使用することは避けてください。スクリーンショットではApp Clipの目的が明確に伝わりません。代わりに、App Clipの価値を理解できる画像や、関連するビジネスの店舗や場所の写真を使います。

**なるべくテキストを使用しない。** ヘッダ画像内のテキストはローカライズできず、読みにくい場合もあります。さらに、カードの見栄えを損なう可能性があります。

**画像の要件に従う。** 1800x1200 pxで、透過処理をしていないPNG画像またはJPEG画像を使用します。

**簡潔な言葉を使う。** App Clipカードにはタイトルとサブタイトルの両方が必要です。利用できるスペース内で、App Clipの目的を明確に、ユーザが一目で読んで理解できるような形で表現してください。タイトルは全角で15文字以下、サブタイトルは全角で28文字以下にする必要があります。

**アクションボタンのタイトルはApp Clipの内容を的確に表現する動詞を使う。** 例えば、「 _表示_ 」、「 _プレイ_ 」、「 _開く_ 」などです。メディアには「 _表示_ 」を使います。App Clipが情報や教育的コンテンツの提供を目的としている場合も、「 _表示_ 」にします。ゲームには「 _プレイ_ 」を使います。その他のApp Clipでは「 _開く_ 」にしてください。

![横に並んだ2枚のApp Clipカード。左はゲームのApp Clipカードで、アクションボタンのタイトルは「プレイ」になっています。左はアプリのApp Clipカードで、アクションボタンのタイトルは「開く」になっています。](https://docs-assets.developer.apple.com/published/190d38f5b0cfc949f40c45bf7efb3800/app-clips-card%402x.png)

## [App Clipコード](/jp/design/human-interface-guidelines/app-clips#App-Clip-Codes)

App Clipコードは、App Clipを見つけてもらうためのベストな手段です。App Clipコードはデザインが独特なので一目でそれと分かり、また、App Clipを素早く安全に起動できます。

![App Clipコード。App Clipのロゴを含むバッジデザインです。](https://docs-assets.developer.apple.com/published/a5b0ac2b9f76d76391473c86a4104ef9/with-appclip-logo%402x.png)App Clipのロゴを含むApp Clipコード

![App Clipコード。App Clipのロゴのないデザインです。](https://docs-assets.developer.apple.com/published/2441534012373af30bf4e6ac94bbcc20/without-appclip-logo%402x.png)App ClipのロゴのないApp Clipコード

App Clipコードでは必ずAppleが提供するデザインを用い、サイズ、配置、プリントのガイドラインに従います。App Clipロゴ（ App Clip）の付いたバッジデザインを選ぶか、スペースの制約がある場合はロゴのないデザインを選びます。App Clipコードの作成にあたっては、デフォルトのカラーの組み合わせを使用しても、カスタムのフォアグラウンドカラーとバックグラウンドカラーを選択してもかまいません。デベロッパ向けのガイダンスは、[App Clipコードの作成](/documentation/AppClip/creating-app-clip-codes)を参照してください。

### [App Clipコードに対する操作](/jp/design/human-interface-guidelines/app-clips#Interacting-with-App-Clip-Codes)

App Clipコードには2つのタイプがあります。 _スキャンのみ_ のタイプとNFCタグが埋め込まれたタイプ（ _NFC付き_ ）です。

![スキャンのみのApp Clipコード。コールアウトで中央のアイコン、ビジュアルコード、App Clipロゴが示されています。](https://docs-assets.developer.apple.com/published/82022d44bda8fab00f44739ecce85f13/scan-only%402x.png)

スキャンのみタイプのApp Clipコードの中央には、カメラアプリまたはコントロールセンターのコードスキャナでApp Clipコードをスキャンするよう伝えるカメラアイコンがあります。NFC付きのApp Clipコードの中央には、デバイスをApp Clipコードにかざすか、コントロールセンターのNFCタグリーダーでApp Clipコードをスキャンするよう伝えるiPhoneアイコンがあります。NFC付きのApp Clipコードは、カメラアプリまたはコントロールセンターのコードスキャナでスキャンすることもできます。例えば以下のような使い方ができます:

  * カフェのメニューにApp Clipコードをプリントし、デバイスをかざしたときにドリンク注文用のApp Clipが即座に起動するようにする。

  * ガソリンスタンドの各給油機にNFC付きのApp Clipコードを貼り付け、デバイスをかざしたときに給油料金を支払うためのApp Clipが起動するようにする。

  * ゲームクリエイターが業界のイベントでApp Clipコードをプリントしたマーケティング資料を配布し、来場者がそのコードをスキャンしたときに最新作のプレイ可能なデモのApp Clipが起動するようにする。

![カフェの店内のイラスト。客がApp Clipコードを利用している様子を示しています。イラストの左側には、テーブル席に座っている2人の客が描かれています。テーブルの中央に置かれたプラカードにApp Clipコードがプリントされています。左の客がカメラでApp Clipコードをスキャンしています。イラストの右側にある円には、スマートフォンの画面とテーブルの上のプラカードが拡大して描かれています。](https://docs-assets.developer.apple.com/published/331753285f06bb59ab3bae929756a505/interacting-coffee-shop-example%402x.png)

### [App Clipコードの表示](/jp/design/human-interface-guidelines/app-clips#Displaying-App-Clip-Codes)

App Clipコードのデザインを始めるにあたっては、App Clipがどのように使われるかを考えてそれに最も適したタイプを選んでください。ユーザが直接触れることができる場所にApp Clipコードを掲示する場合は、NFC付きのタイプを使います。例えば以下のような使い方ができます:

  * 飲食店のテーブルの上

  * 小売店のレジ付近

  * 店先のショーウインドウ

  * 看板

  * ギフトカードやクーポン

ユーザが直接触れることができない場所にApp Clipコードを掲示する必要がある場合や、デジタルで表示する必要がある場合は、スキャンのみタイプのApp Clipコードを使います。例えば以下のような使い方ができます:

  * ポスターやチラシ

  * カウンターの後ろや、店先の近づけない場所にある看板

  * デジタルディスプレイなどのデジタル素材、メール、ソーシャルメディアに投稿する画像

どちらのタイプを使う場合でも、スキャンの信頼性を確保できるよう、App Clipコードの掲示場所を慎重に検討することが重要です。

**スペースが許すならApp Clipロゴを含める。** ロゴがあると、App ClipコードからApp Clipを起動できることが明確に分かります。ただし、空白領域の要件を満たせないようであれば、App ClipロゴのないApp Clipコードデザインを使います。使い捨ての紙製品やプラスチック製品、ギャンブルやアルコール飲料と関係するアイテムにApp Clipコードを含める場合も、App Clipロゴのないデザインを使ってください。例えば、トランプ、ポーカーチップ、バーのコースターにはApp ClipロゴのないApp Clipコードを使ってください。App Clipロゴは、必ず、App Clipコードの下に表示されるバッジデザインに含め、App Clipロゴ単体で使用することは絶対にしないでください。

**App Clipコードは平面または円柱面にのみ配置する。** App Clipコードをスクーターのハンドルバーのような円柱面に掲示する場合は、App Clipコードの幅が円柱の外周の6分の1を超えないようにしてください。

![円周の図形。円柱面が示されています。円周を6等分した線が描かれています。セグメント1つ分がApp Clipコードの幅の上限となります。App Clipコードが円柱面の外周の6分の1（60度）を超えないようにしてください。](https://docs-assets.developer.apple.com/published/63644f0fdf2b4532e21c14c2b224855d/app-clips-slice%402x.png)

**スムーズにスキャンできるように、App Clipコードをできる限り平らな状態に保つ。** スキャンのしやすさが損なわれないように、変形しやすい素材（紙やプラスチック、布など、簡単に折れたりしわになったりするもの）の上にApp Clipコードを配置することは避けましょう。バッグや柔らかい箱など変形しやすいものの上にApp Clipコードを掲示しなければならない場合は、カードのような固いものにApp Clipコードをプリントし、それを貼り付けます。App Clipコードのステッカーを作成する場合は、平面にしっかりと貼り付くようにしてください。

**確実にスキャンできる場所にApp Clipコードを掲示する。** 例えば、スキャンのみタイプのApp Clipコードは、確実にスキャンできるよう、十分に明るい場所に掲示します。また、ユーザが正面からスキャンできないような場所には掲示しないでください。

**App Clipコードのスキャンの妨げになるようなことをしない。** App Clipコードにテキストやロゴや画像を重ねないでください。App Clipコードを絶対にアニメーションさせたり暗くしたりしないでください。

**App Clipコードは直立した状態で表示する。** 生成されたApp Clipコードを回転させたり、中央のグリフを斜めに表示したりしないでください。

![正しく表示されたApp Clipコード。直立しています。](https://docs-assets.developer.apple.com/published/a6eaaa833a98678b2b93f910f149bb6e/upright-display-right%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![App Clipコードの配置のNG例。左に90度回転しています。](https://docs-assets.developer.apple.com/published/5897608f22eb0d296f1a8189c1f2e38b/upright-display-wrong-1%402x.png)

![丸に囲まれたバツ印が無効なApp Clipコードであることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![App Clipコードの配置のNG例。右に135度回転しています。](https://docs-assets.developer.apple.com/published/d4b3a7a3d5685fbec4194deb55bbb0c9/upright-display-wrong-2%402x.png)

![丸に囲まれたバツ印が無効なApp Clipコードであることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

**極端に小さいApp Clipコードを作成しない。** App Clipコードは、必ず以下の仕様に従って作成してください。

タイプ| 最小サイズ  
---|---  
プリント| 直径3/4インチ（1.9 cm）以上。  
デジタル| 256×256 px以上。PNGまたはSVGファイルを使用します。  
NFC付きApp Clipコード| 埋め込みNFCタグは、直径35 mm以上またはそれに相当するサイズにする必要があります。例えば、埋め込みNFCタグの直径が35 mmの場合、プリントするApp Clipコードの直径は1.37インチ（3.48 cm）以上にする必要があります。  
  
![バッジデザインを使用したApp Clipコード。直径は最小値である3/4インチ（1.9 cm）です。](https://docs-assets.developer.apple.com/published/96bb0500f4240a47f49b7cfc9bf0eedb/sizing-minimum-rectangle%402x.png)

![App Clipロゴのないデザインを使用したApp Clipコード。直径は最小値である3/4インチ（1.9 cm）です。](https://docs-assets.developer.apple.com/published/8a30e531015e7dbfd0b936e398231db6/sizing-minimum-circular%402x.png)

App Clipコードのサイズを決定する際には、コードサイズが、デバイスからコードまでの距離の20分の1以下にならないようにします。スキャンの信頼性を確保するため、可能であれば10分の1以上にしてください。例えば、ユーザが40インチ（101 cm）離れてスキャンするApp Clipは、直径を4インチ（10.16 cm）以上にする必要があります。

App ClipコードをQRコードなどほかのスキャン対象物の近くに掲示する場合は、App Clipコードのサイズを少なくともほかのコードやアイテムのサイズと同じにしてください。

![App ClipコードとQRコードが横に並んだ図。2つが同じサイズであることを示す赤いガイドが表示されています。](https://docs-assets.developer.apple.com/published/b693a5616cb7a4b58895496c6b834b2d/app-clip-with-qr-code%402x.png)

**App Clipコードとそれに隣接するApp Clipコード、グラフィックス、マテリアルの間に十分なスペースを設ける。** App Clipコードの周囲には、中央のグリフから円形のコード部分までの距離と同じかそれ以上の幅の空白領域を確保します。App Clipコードを別のApp Clipコードやほかの機械読み取り式コードと並べて配置する場合は、各コードのスキャンの信頼性を確保するため、十分な間隔を空けてください。

![左にバッジデザインのApp Clipコード、右にApp ClipロゴのないApp Clipコードが示された図。それぞれのApp Clipコードを囲んでいる赤いガイド線が、必要な空白領域を示しています。](https://docs-assets.developer.apple.com/published/60ce57295e138b8c399d9c229238f40d/app-clip-spacing%402x.png)

### [使い方を分かりやすく伝える](/jp/design/human-interface-guidelines/app-clips#Using-clear-messaging)

どうすればApp ClipコードからApp Clipを起動できるかを説明する分かりやすい文言を添えましょう。特に、App Clipロゴなしのデザインを使う場合はこれが必要です。例えば、メールやポスターの中のApp Clipコードの近くに、操作方法を伝える文言を添えます。推奨の文言を使うか、独自の文言を考えます。いずれにしても、必ずシンプルで明確な文言にしてください。

![カフェのテーブル席に座っている2人の客のイラスト。テーブルの中央に置かれたプラカードにApp Clipコードがプリントされています。イラストの右側にある円の中にプラカードが拡大して描かれています。プラカードには、App Clipコードに加えて、コードの周囲に次のテキストがプリントされています。「ご注文はこちらから。iPhoneをメニューにかざすとお食事をご注文いただけます」。](https://docs-assets.developer.apple.com/published/0f4906c5d5a71adda59d4408ede08d04/clear-messaging%402x.png)

スキャンのみタイプのApp Clipコードの場合、以下のような文言で操作方法を説明できます:

  * スキャンしてみてください。[_App Clipで実行できるタスク_]できます。

  * iPhoneやiPadのカメラでスキャンしてみてください。[App Clipで実行できるタスク]できます。

NFC付きのApp Clipコードの場合、以下のような文言で操作方法を説明できます:

  * スキャンしてみてください。[_App Clipで実行できるタスク_]できます。

  * お手持ちのiPhoneを[_スキャン対象物の名前_]にかざしてみてください。[_App Clipで実行できるタスク_]できるApp Clipが起動します。

詳しくは、[NFC](/jp/design/human-interface-guidelines/nfc)を参照してください。

**App ClipとApp Clipコードに言及する際は[Apple商標および著作権使用に関するガイドライン](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)に従う。**例えば、アプリ名または画像内でAppleの商標を使用することは禁止されています。また、App ClipまたはApp Clipコードという語を使う場合は常にタイトルケースにしなければなりません。詳しくは、[法的要件](/jp/design/human-interface-guidelines/app-clips#Legal-requirements)を参照してください。

### [App Clipコードのカスタマイズ](/jp/design/human-interface-guidelines/app-clips#Customizing-your-App-Clip-Code)

[App Store Connect](https://appstoreconnect.apple.com)または[App Clipコードジェネレータ](https://developer.apple.com/app-clips/resources/)コマンドラインツールを使用してApp Clipコードを作成します。安定してスキャンできるようにするため、以下のベストプラクティスに従ってください。

![4つのApp Clipバッジ。さまざまな色を使っています。左の2つはバッジデザイン、右の2つはApp Clipのロゴのないデザインです。](https://docs-assets.developer.apple.com/published/02d96548534ce28b92754477aadbf9bb/app-clips-customizing%402x.png)

**必ず、生成されたApp Clipコードを使う。** 独自にApp Clipコードをデザインしないでください。また、生成されたApp Clipコードには一切の変更を加えないでください。フィルタを適用したり、色を濃くしたり、グロー、シャドウ、グラデーション、反射を追加したりしないでください。安定してスキャンできなくなる原因になります。生成されたApp Clipコードを拡大/縮小する場合は、生成されたコードのアスペクト比を変更しないでください。また、線の幅などApp Clipコードのすべての属性を拡大/縮小する必要があります。

![無効なApp Clipコードの図。アスペクト比が変更されています。](https://docs-assets.developer.apple.com/published/2243d4c0011526cae9bd3d69e62907ae/customizing-wrong-1%402x.png)

![丸に囲まれたバツ印が無効なApp Clipコードであることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![無効なApp Clipコードの図。バックグラウンドカラーが単色ではなくグラデーションになっています。](https://docs-assets.developer.apple.com/published/6578f646c8aae8d6ac64ef965b783175/customizing-wrong-2%402x.png)

![丸に囲まれたバツ印が無効なApp Clipコードであることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![無効なApp Clipコードの図。ドロップシャドウエフェクトが適用されています。](https://docs-assets.developer.apple.com/published/658d3fafbc3dfdd11dc26f1b5a7aee48/customizing-wrong-3%402x.png)

![丸に囲まれたバツ印が無効なApp Clipコードであることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

**正確にスキャンできるだけのコントラストが得られるカラーを組み合わせる。** App Clipコードでは、フォアグラウンドカラー、バックグラウンドカラー、3番目のカラーという3つのカラーを使います。3番目のカラーは、フォアグラウンドカラーとバックグラウンドカラーに基づいて生成されます。[App Store Connect](https://appstoreconnect.apple.com)と[App Clipコードジェネレータ](https://developer.apple.com/app-clips/resources/)コマンドラインツールには両方とも、デフォルトの色の組み合わせが用意されていますが、カスタムのフォアグラウンドカラーとバックグラウンドカラーを選択することもできます。ただし、スキャンの質を下げるようなカスタムカラーの組み合わせは選べません。カラーの選択が適切でない場合、App Store ConnectでもコマンドラインツールでもApp Clipコードは生成されません。効果的なカラーの組み合わせを選べるように、どちらのツールにも、カスタムのバックグラウンドカラーに基づいて別のフォアグラウンドカラーを提案する機能が備わっています。詳しくは、[App ClipコードジェネレータでApp Clipコードを作成する](/documentation/AppClip/creating-app-clip-codes-with-the-app-clip-code-generator)および[App Store ConnectでApp Clipコードを作成する](/documentation/AppClip/creating-app-clip-codes-with-app-store-connect)を参照してください。

![バッジデザインのApp Clipコードの図。コールアウトでバックグラウンドカラー、フォアグラウンドカラー、生成されたカラーが示されています。](https://docs-assets.developer.apple.com/published/5c4cff5f8c850d529159cedd289b0bab/app-clip-colors%402x.png)

## [プリントのガイドライン](/jp/design/human-interface-guidelines/app-clips#Printing-guidelines)

App ClipコードはApp Clipを起動するのにベストな方法です。したがって、スキャンの信頼性を長期間維持できるApp Clipコードを作成して掲示することが重要になります。App Clipコードは自分でプリントすることも、[RR Donnelley](https://touchless.acc.rrd.com/)のような専門のプリントサービスに依頼することもできます。

プリントされたApp Clipコードを配布する前に、いろいろな角度からスキャンできることを必ずテストしてください。

**ざらつきのない高品質の素材にプリントする。** App Clipコードはマット仕上げの素材にプリントしてください。薄いラミネート仕上げやそのような素材のほか、つや、光沢、反射、ホログラムの表面加工も避けます。App Clipコードがプリントされた素材をラミネート加工する必要がある場合は、輝きや反射を抑えるマットラミネートを使います。App Clipコードを屋外に掲示する場合、日光や風雨などにさらされて色落ちしないように耐UV性の素材やコーティングを使います。専門のプリントサービスに依頼するときは、フレキソ印刷を指定するのが最適です。デスクトッププリンタを使って自分でApp Clipコードをプリントする場合は、インクジェットプリンタが最適です。

**高解像度画像を使い、それに対応するプリンタ設定にする。** SVGファイルをラスタライズする場合は、画像の解像度を600 ppi以上に設定し、App Clipコードを300 dpi以上の解像度でプリントしてください。高品質のプリントを保証するため、プリントの前にプリンタの水平調整やキャリブレーションを検討してください。さらに、カラーチャネル調整の不足、不正確なガンマ値、アーチファクトなど品質が低下する要因を取り除き、楕円その他の形状にApp Clipコードが歪まないようにも注意します。レシートプリンタを使う場合は、できる限り用紙いっぱいにApp Clipコードをプリントしてください。

**生成されたSVGファイルをCMYK画像に変換する際にカラーを適切に設定する。**[App Clipコードジェネレータ](https://developer.apple.com/app-clips/resources/)コマンドラインツールと[App Store Connect](https://appstoreconnect.apple.com)は両方とも、App ClipコードをsRGB色空間のSVGファイルとして生成します。このSVGファイルに適合するカラーでプリントするには、sRGB画像をCMYK画像に変換します。変換実行時には、相対色度（メディア相対）インテントを使います。CMYKプリンタでは「Generic CMYK ICCプロファイル」を、CMYKOVプリンタでは「Gracol 2013 ICCプロファイル」を使用し、カラー許容差CIELab Delta Eは2.5としてください。

**白黒プリンタを使用する場合は、グレイスケールのApp Clipコードのみを生成する。** カラーで生成されたコードをグレイスケールでプリントすると、信頼性が低下する可能性があります。

**NFC付きのApp ClipコードではType 5 NFCタグを選択する。** 埋め込みNFCタグは、直径35 mm以上またはそれに相当するサイズにする必要があります。

**App Clipコードを大量に作成する場合はプリントのワークフローを入念にテストし、プリントされたApp Clipコードを確認する。** 例えば、費用をかける必要はないので、一部のコードを少しだけプリントしてみます。このとき、App Clipコードをプリントするプリントテンプレートには、エンコードされている呼び出しURLとSVGファイル名を各コードの横に表示できるように余白を多めに設け、このURLとファイル名を使ってプリントの確認を行います。

[App Clipコードジェネレータ](https://developer.apple.com/app-clips/resources/)ツールまたは[App Store Connect](https://appstoreconnect.apple.com)で多数のApp Clipコードを作成する場合は、おそらく専門のプリントサービスに依頼することになるでしょう。そうすることにした場合は大量のSVGファイルを処理する必要が出てきます。とはいえ、App Clipコードを見ただけでは、どのApp ClipコードがどのURLをエンコードしているかは分からないので、SVGファイルと呼び出しURLの対応関係を確認できるファイルが必要になります。どのような状況でも、ファイル管理、バージョン管理、変更トラッキングに注意を払うことがプリントプロジェクトの失敗を避ける鍵になります。詳しくは、[本番環境用に複数のApp Clipコードを準備する](/documentation/AppClip/preparing-multiple-app-clip-codes-for-production)を参照してください。

### [プリンタの調整の検証](/jp/design/human-interface-guidelines/app-clips#Verifying-your-printers-calibration)

スキャン体験が安定するかどうかは、プリントされたApp Clipコードの品質次第です。プリントしたApp Clipコードのスキャン体験を安定させ、また、高品質のApp Clipコードをプリントできないプリンタを使用しないようにするには、Appleが公開している[プリンタ調整テストシート](https://developer.apple.com/app-clips/resources/printer-calibration-test-sheets.zip)を使ってプリンタの設定とプリント品質を検証してください。

**デフォルトのカラーの組み合わせごとにテキストボックスが表示されるプリンタ調整テストシートを使って、選択したカラーの組み合わせのプリント品質を検証する。** シートに示された手順に従って、正しい倍率でプリントし、お使いのプリンタで高品質のApp Clipコードを作成できることを検証してください。

**2つのグレイスケールバーが表示されたプリンタ調整テストシートをプリントして、プリンタのグレイスケール設定を検証する。** 薄かったり少しも見えなかったりするグレイのカラーがある場合はプリンタの調整が必要と考えられます。あるいは、そのプリンタでは安定してスキャンできるApp Clipコードをプリントできない可能性もあります。

## [法的要件](/jp/design/human-interface-guidelines/app-clips#Legal-requirements)

App Store Connect内、またはApp Clipコードジェネレータコマンドラインツールを使って作成され、かつ以下のガイドラインに従う、Appleが提供するApp Clipコードのみが使用を認められます。

App Clipコードは、App Clipが提供されていることを示すために使用することが認められています。Appleは自己の裁量により、App Clipコードのデザインを随時アップデートすることがあります。

App Clipの提供を終了した場合は、その提供を終了したApp Clipに対応するApp Clipコードの掲示も終了します。

会社名や商品名の一部としてApp Clipコード（Appleロゴ、App Clipマーク、App Clipコードのデザインが含まれ、これらに限定されない）を使用することは禁止されています。App Clipコードまたはそれに含まれる一切の要素について著作権または商標登録を要求することも禁止されています。

このガイドラインで説明されているApp Clipコードを、AppleまたはApp Clipに関連する業務上の信用、価値、評判を低下させたり、弱めたり、損なったりする可能性の高い方法で使用してはなりません。第三者の商標その他の財産権を侵害したり、損なったりする可能性が高い場合や、商品またはサービスの提供・開発元に関して混乱を引き起こす可能性が高い場合も同様です。

Appleは、この文書に従って使用に供される資料に含まれる商標、著作権、その他の知的財産権（App Clipコードとそれに含まれるあらゆる要素が含まれ、これらに限定されない）に対するあらゆる権利を留保します。

App Store Connect内、またはApp Clipコードジェネレータコマンドラインツールを使って作成されたApp Clipコードにシンボルを追加しないでください。

いかなるApple商標も翻訳しないでください。Appleの商標は、英語以外の言語のテキスト内でも英語のままにする必要があります。Appleの許可がある場合は、法律に基づく情報およびクレジット表記（ただし、商標ではない）の翻訳を米国外で配布される資料内で使用できます。

Appleの商標の使用について詳しくは、[Apple商標および著作権使用に関するガイドライン](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/app-clips#Platform-considerations)

 _iOS、iPadOSに追加の考慮事項はありません。macOS、tvOS、visionOS、watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/app-clips#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/app-clips#Related)

[Apple Pay](/jp/design/human-interface-guidelines/apple-pay)

[Appleでサインイン](/jp/design/human-interface-guidelines/sign-in-with-apple)

[Apple商標および著作権使用に関するガイドライン](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/app-clips#Developer-documentation)

[App Clips](/documentation/AppClip)

[App Store Connect](https://appstoreconnect.apple.com/)

#### [ビデオ](/jp/design/human-interface-guidelines/app-clips#Videos)

[](https://developer.apple.com/videos/play/wwdc2021/10012)

[](https://developer.apple.com/videos/play/wwdc2021/10013)

## [変更履歴](/jp/design/human-interface-guidelines/app-clips#Change-log)

日付| 変更内容  
---|---  
2025年6月09日| デモのApp Clipを含めるようにガイダンスを更新。  
2023年5月02日| ガイダンスを1ページに統合しました。
