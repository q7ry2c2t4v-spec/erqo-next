# HomeKit

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/homekit

# HomeKit

HomeKitは、ユーザがiPhone、iPad、Apple Watch、MacのSiriやホームアプリを使って施設内のネットワーク接続型アクセサリを安全に制御できるようにするテクノロジーです。

![HomeKitアイコンのスケッチ。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる青色になっています。](https://docs-assets.developer.apple.com/published/e34278493a4ef99561c9982028c7a3b7/technologies-HomeKit-intro%402x.png)

iOSでは、ユーザはホームアプリを使ってアクセサリの管理と設定をすることもできます。

iOS、tvOS、またはwatchOSのアプリをHomeKit（さらにはホームアプリ）と連係させれば、体験をカスタマイズしたり、アクセサリ専用の体験を提供したりできます。例えば、以下のようなことができます:

  * アクセサリの設定、名称設定、整理をユーザができるようにする

  * アクセサリの詳細な設定と制御を許可する

  * アクセサリのカスタム機能を利用できるようにする

  * 強力なハンズフリーオートメーションの作成方法を示す

  * サポートを提供する

デベロッパ向けのガイダンスは、[HomeKit](/documentation/HomeKit)を参照してください。MFiのライセンスを受けている場合は、アクセサリのパッケージの名称とメッセージに関するガイダンスを[MFiポータル](https://mfi.apple.com)で確認してください。

## [用語とレイアウト](/jp/design/human-interface-guidelines/homekit#Terminology-and-layout)

HomeKitでは、ホームがオブジェクトの階層としてモデリングされ、各オブジェクトを指す用語が定義されます。ホームアプリでは、ユーザが音声、アプリ、オートメーションでアクセサリを直感的に操作できるようにするため、HomeKitのこのオブジェクトモデルおよび用語の使用を徹底しています。

アプリでも、HomeKitで定義される用語とオブジェクトモデルを使うことが重要です。そうすることでユーザの理解を助け、ホームオートメーションに対する心理的なハードルを下げることができます。

HomeKitのモデルの階層の最上位は、[ホーム](/jp/design/human-interface-guidelines/homekit#Homes)オブジェクトです。これには、[部屋](/jp/design/human-interface-guidelines/homekit#Rooms)、[アクセサリ](/jp/design/human-interface-guidelines/homekit#Accessories-services-and-characteristics)、[ゾーン](/jp/design/human-interface-guidelines/homekit#Zones)など、すべてのオブジェクトが含まれます。ホームが複数ある場合は、それぞれのホームが個々の階層の最上位になります。

**HomeKitの階層モデルに従う。** アプリのUIでアクセサリを部屋やゾーンごとに分けない場合でも、アクセサリの設定や操作をガイドするときにはHomeKitのモデルを基準にするとユーザにとって便利です。SiriやHomePodに「Siri、上の階の照明を点けて」や「ここは暗いね」などの音声コマンドで話しかけてアクセサリを操作するためには、アクセサリがある場所を把握しておく必要があるためです。詳しいガイダンスは[Siriの操作](/jp/design/human-interface-guidelines/homekit#Siri-interactions)を参照してください。

**アクセサリ関連のHomeKit情報をユーザが見つけやすくする。** アクセサリに基づいてアプリを組み立てている場合でも、見つけにくい設定画面にアクセサリのゾーンや部屋などのHomeKit情報をしまい込まないでください。アクセサリの詳細ビューで関連のHomeKit情報を簡単に確認できるようにすることをおすすめします。

**複数のホームがあるケースを考慮に入れる。** アプリが1人のユーザに複数のホームがあるケースに対応していなくても、アクセサリの詳細ビューにホームの情報を表示することをおすすめします。

**何度も同じホーム設定をさせない。** ホームの構造の捉え方がホームアプリと異なる場合でも、ホームの全部または一部の再設定を求めたり、同じ設定画面を見せたりしてユーザを戸惑わせないようにしましょう。必ず、ユーザがホームアプリで行った設定に従うようにし、その情報を自身のアプリのUIで分かりやすく表示する方法を検討してください。

### [ホーム](/jp/design/human-interface-guidelines/homekit#Homes)

HomeKitにおける _ホーム_ とは、物理的な自宅やオフィスなど、ユーザに関連する場所を表します。1人のユーザに複数のホームがある場合もあります。

### [部屋](/jp/design/human-interface-guidelines/homekit#Rooms)

 _部屋_ は、ホームの物理的な部屋を表します。部屋は広さや場所などの属性は持たず、ユーザにとって意味を持つ名前でしかありません（例: _寝室_ 、 _オフィス_ ）。部屋にアクセサリを割り当てると、「Siri、寝室以外のすべての照明を点けて」や「Siri、キッチンと玄関の照明を点けて」といった音声コマンドを利用できるようになります。

### [アクセサリ/サービス/キャラクタリスティック](/jp/design/human-interface-guidelines/homekit#Accessories-services-and-characteristics)

 _アクセサリ_ とは、シーリングファン、照明、錠、カメラなど、ネットワーク接続型の物理的なホームアクセサリを表します。HomeKitではアクセサリの種類（サーモスタット、ファン、照明など）を _カテゴリ_ と呼びます。通常、アクセサリのカテゴリはメーカー側で割り当て済みですが、必要であればアプリでユーザがこの割り当てを行えるようにすることもできます。例えば、ファンや照明に接続されたスイッチは、その制御対象のアクセサリと同じカテゴリに割り当てる必要があります。

アクセサリの制御可能な部分を _サービス_ と呼びます（ネットワーク接続型照明のスイッチなど）。複数のサービスを持つアクセサリもあります。例えば、照明と扉を別々に制御できるネットワーク接続型ガレージドアや、上下のコンセントを別々に制御できるネットワーク接続型コンセントなどが考えられます。アプリのUIでは _サービス_ という言葉は使わず、サービスを表す名前を使います（ _ガレージドアオープナー_ 、 _シーリングファンの照明_ など）。Siriでホームのアクセサリを制御するときはアクセサリ名ではなくこのサービス名を使います。命名の詳しいガイダンスは[ユーザが適切な名称を付けられるようにする](/jp/design/human-interface-guidelines/homekit#Help-people-choose-useful-names)を参照してください。

 _キャラクタリスティック_ とは、サービスの制御可能な属性のことです。例えば、シーリングファンのファンサービスなら回転速度のキャラクタリスティック、照明サービスなら明るさのキャラクタリスティックが考えられます。アプリのUIではキャラクタリスティックという言葉は使わず、属性を表す用語を使います（ _回転速度_ 、 _明るさ_ など）。

 _サービスグループ_ とは、まとめて制御したいアクセサリサービスのグループを表します。例えば、リビングの一角にある1つのフロアランプと2つのテーブルランプの3つのサービスをすべて _読書灯_ という1つのサービスグループに割り当てるとします。この場合、ユーザは _読書灯_ サービスグループを使うことで、この3つの照明をリビングのその他すべての照明と分けて制御できます。

### [アクションとシーン](/jp/design/human-interface-guidelines/homekit#Actions-and-scenes)

 _アクション_ とは、サービスのキャラクタリスティックを変えることです。ファンの回転速度や照明の明るさを調整することなどがこれに当たります。アクションはユーザまたはオートメーションによって開始されます。

 _シーン_ は、1つ以上のアクセサリの1つ以上のサービスを制御するアクションのグループです。例えば、リビングのシェードを下げて照明を暗くする _映画タイム_ というシーンや、照明を点けてシェードを上げ、キッチンのコーヒーメーカーを起動する _おはよう_ シーンなどが考えられます。

ヒント

HomeKit APIではシーンのことを _アクションセット_ と呼びますが、アプリのUIでは、必ず _シーン_ という用語を使うようにしてください。

### [オートメーション](/jp/design/human-interface-guidelines/homekit#Automations)

 _オートメーション_ を設定すると、ユーザが場所を移動したとき、1日のある時間になったとき、別のアクセサリがオン/オフになったとき、センサーが何かを検知したときなど、アクセサリを特定の状況に反応させることができます。例えば、オートメーションによって日没時や帰宅時に家の照明を点けることができます。

### [ゾーン](/jp/design/human-interface-guidelines/homekit#Zones)

 _ゾーン_ とは、ホームのある領域を表します。 _上の階_ や _下の階_ のように、複数の部屋を含めることができます。ゾーンの設定は必須ではありませんが、ゾーンを設定することで複数のアクセサリを一度に制御できるようになります。例えば、下の階のすべての照明を _下の階_ という名前のゾーンに割り当てると、「Siri、下の階のすべての照明を消して」といった音声コマンドを使えるようになります。

## [設定](/jp/design/human-interface-guidelines/homekit#Setup)

**慣れ親しんだ操作で扱えるようにシステムが提供する設定フローを使用する。** HomeKitの設定フローなら、アクセサリの名称設定、ネットワークへの接続、HomeKitとのペアリング、部屋やサービスカテゴリの割り当て、よく使う項目の指定をわずか数ステップで完了できるので、従来の設定フローよりも高速です。システムが提供する設定フローをできる限り利用することで、独自のカスタム機能をアピールすることに集中できます。デベロッパ向けのガイダンスは、[`performAccessorySetup(using:completionHandler:)`](/documentation/HomeKit/HMAccessorySetupManager/performAccessorySetup\(using:completionHandler:\))を参照してください。

**なぜユーザのホームデータへのアクセスが必要なのかを説明する。** 目的文字列を作成し、ホームデータへのアクセスが必要な理由を説明する文言を追加します（例: 「Apple HomeアプリやSiriを使って、お使いのすべてのAppleデバイスでこのアクセサリを制御できるようにします」）。

**アカウントの作成や個人情報の入力をユーザに要求しない。** 必要な情報がある場合はHomeKitに保持されているものを使用してください。アカウントを作成することでクラウドサービスなどのサービスを追加で利用できるようになる場合は、アカウント設定を任意にし、最初のHomeKit設定が終わってから提示しましょう。

**ユーザの設定を尊重する。** ユーザがHomeKitを使ってアクセサリを設定することにした場合は、HomeKitの設定フローの途中でほかのプラットフォームの設定を強制しないようにしましょう。クロスプラットフォームの設定を求めると、アクセサリをすぐに使い始めることができず、また、アクセサリを制御する手段がありすぎるためにユーザが戸惑ってしまう可能性があります。

**アクセサリ独自の設定手順をいつどのように表示するかを慎重に検討する。** 最初は必ずシステムが提供する設定フローを示しましょう。それから、アクセサリの基本機能を有効にしたあとで、標準設定後のカスタムフローの中でアクセサリの独自機能を紹介し、最大限に活用するための方法を示します。例えば照明メーカーのアプリなら、ユーザのライブラリ内の写真からスキャンしたキーカラーを使って照明シーンをパーソナライズできるようにするなどです。

### [ユーザが適切な名称を付けられるようにする](/jp/design/human-interface-guidelines/homekit#Help-people-choose-useful-names)

**アクセサリに適したサービス名を提案する。** Siriの音声コントロールに最適とはいえないサービス名が作成されたことをアプリで検知した場合には、多くの人にとって最適と思われる代案を示しましょう。ただし、サービス名として会社名やモデル番号を提案することはしないでください。

**ユーザが選んだ名前がHomeKitの命名規則に準拠していることをチェックする。** アプリでサービスの名称変更をユーザに許可する場合は、変更後の名前が命名規則に準拠していることを確認してください。（元の名称はシステムが提供する設定フローで自動的にチェックされます。）入力された名前が1つ以上の規則に違反していた場合は、正しくない部分を簡単に説明し、適切な代案を示します。命名規則は以下の通りです:

  * 2バイト文字、英数字、空白、アポストロフィのみを使用する。

  * 最初と最後には2バイト文字または英数字を使用する。

  * 絵文字を含めない。

| サービス名の例  
---|---  
![丸に囲まれたチェックマークは正しい使い方を示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| 読書灯  
![丸に囲まれた×印は不適切な使い方を示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)| 📚 ランプ  
![丸に囲まれたチェックマークは正しい使い方を示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| 2つ目のガレージドア  
![丸に囲まれた×印は不適切な使い方を示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)| #2 ガレージドア  
  
**場所の情報を含む名前をユーザが作成しないようにする。** キッチンに取り付けた照明に「キッチンの照明」という名前を付けるのはごく自然なことですが、サービス名に部屋名を含めると、音声でアクセサリを制御するときに予想外の結果になってしまうことがあります。サービス名に場所の情報が重複して入っていることをアプリで検知し、ユーザに修正を促せるようにしましょう。例えば、設定後の手順でサービス名から部屋名やゾーン名を削除し、ユーザにはアクセサリをその部屋またはゾーンに割り当てるように促します。

## [Siriの操作](/jp/design/human-interface-guidelines/homekit#Siri-interactions)

HomeKitは、音声コマンドによる高性能なハンズフリー制御に対応しています。ユーザがSiriを使ってホーム内のアクセサリやサービス、ゾーンを素早く効率的に操作できるようにしましょう。

**Siriを使ったアクセサリの制御方法について設定時に音声コマンドの例を示す。** 新しいアクセサリの設定完了後すぐに、ユーザが選んだサービス名を入れたSiriのフレーズをいくつか例示して、そのフレーズを試すように促せます。

**設定後に、もっと高度なSiriコマンドをユーザに教える。** さまざまな自然な言い回しを用いてSiriやHomePodでアクセサリを制御できることをユーザが知っているとは限りません。設定の完了後に、アプリ内の適切な場所でそうした種類のコマンドをユーザに伝えるようにしましょう。例えば、シーンの詳細表示では _「Hey Siri、“映画タイム”をセットして」_ のように言えることをユーザに伝えます。

Siriは、ホーム、部屋、ゾーン、サービス、シーンの名前を認識できるだけでなく、アクセサリのカテゴリやキャラクタリスティックなどの情報をもとにサービスを特定することもできます。例えば、「 _明るく_ 」や「 _暗く_ 」などの言葉が使われていれば、たとえサービス名が言及されていなくても、Siriはそれが明るさのキャラクタリスティックを持つサービスに対するコマンドであることを認識できます。

Siriコマンドがいかに強力で柔軟であるかがよく分かるアクセサリ制御フレーズの例を以下に示します。

フレーズ| Siriの理解  
---|---  
「フロアライトを点けて」| サービス（ _フロアライト_ ）  
「入口のカメラを見せて」| サービス（ _入口のカメラ_ ）  
「照明を点けて」| アクセサリのカテゴリ（ _照明_ ）  
「リビングの照明を点けて」| 部屋（ _リビング_ ）  
アクセサリのカテゴリ（ _照明_ ）  
「リビングを少しだけ明るくして」| 部屋（ _リビング_ ）  
アクセサリのカテゴリ（言外）  
明るさのキャラクタリスティック（ _明るく_ ）  
「ダウンライトを点けて」| サービスグループ（ _ダウンライト_ ）  
「上の階の照明を消して」| アクセサリのカテゴリ（ _照明_ ）  
ゾーン（ _上の階_ ）  
「寝室と子ども部屋の照明を暗くして」| アクセサリのカテゴリ（ _照明_ ）  
明るさのキャラクタリスティック（ _暗く_ ）  
部屋（ _寝室_ 、 _子ども部屋_ ）  
「おやすみを実行して」| シーン（ _おやすみ_ ）  
「リビングに誰かいる?」| アクセサリのカテゴリ（言外）  
人検知のキャラクタリスティック（言外）  
「セキュリティシステムは発動した?」| アクセサリのカテゴリ（ _セキュリティシステム_ ）  
「ガレージドアを開けっぱなしにしちゃったかな?」| アクセサリのカテゴリ（ _ガレージドア_ ）  
開放のキャラクタリスティック（ _開放_ ）  
「タホ湖の家の照明を消し忘れたかな?」| アクセサリのカテゴリ（ _照明_ ）  
ホーム（ _タホ湖の家_ ）  
「ここは暗いね」| 現在のホーム（ _ここ_ ）  
現在の部屋（HomePod経由）  
アクセサリのカテゴリ（言外）  
  
**ユーザにゾーンやサービスグループの作成を提案する（そうすることが理にかなっている場合）。** ユーザにとって、特定の状況と結び付いた音声コマンドを組み合わせてアクセサリを制御した方がよい場合は、そうした種類のコマンドを提案して設定を支援できます。例えば、照明、スイッチ、サーモスタットなどのアクセサリを提供している場合は、「上の階」というゾーンや「メディアセンター」というサービスグループの設定を提案して、ユーザが「Siri、上の階の照明を消して」や「Siri、メディアセンターを起動して」などのコマンドを使えるようにします。

**ショートカットはHomeKitが対応していないアクセサリ専用機能にのみ提供する。** HomeKitでは、特別な設定をしなくても日常会話のような自然な言い回しでアクセサリを制御できるため、HomeKitの機能と重複するショートカットを示されてもユーザは戸惑ってしまいます。そのようなことはせず、アプリで提供する補足的な機能としてショートカットを用意しましょう。例えば、アプリで取り扱っているエアコンフィルターをユーザがよく注文するようなら、「エアコンのフィルターを注文」のようなショートカットを用意できます。ショートカットに使えるフレーズを提供する方法については、[ショートカットと提案](/jp/design/human-interface-guidelines/siri#Shortcuts-and-suggestions)を参照してください。

**アプリがHomeKitとショートカットの両方に対応している場合はその音声コマンドの違いを分かりやすく示す。** 複数の音声コマンドが示されるとユーザが混乱する可能性があります。ショートカットで何ができるのかを明確に提示してください。また、すでにHomeKitが対応しているシーンやアクションに対してショートカットの作成を促すことはしないでください。

## [カスタム機能](/jp/design/human-interface-guidelines/homekit#Custom-functionality)

アプリは、アクセサリ独自の機能についてユーザに知ってもらう絶好の場所です。例えば、カラーをさまざまに変えられる照明のアプリなら、ユーザが写真から取り込んだカラーを使ってHomeKitのシーンを作成できるようにするのも1つの方法です。

**アプリでできることとホームアプリで実行すべき操作の区分、および各操作のタイミングを明確に提示する。** 例えば、照明のみに対応しているアプリの場合は、照明の明るさを落とすだけでなく、同時にシェードを下げてテレビを特定の入力に切り替える「映画タイム」シーンの作成を促してみましょう。これを行うには、まず照明アクセサリのアクション（この場合は「明るさを落とす」）のみを含むシーンを設定するようにユーザをガイドします。その後、ホームアプリを開いてこのシーンにHomeKitと互換性のあるシェードとテレビを追加するように促します。ホームアプリへの言及の仕方については、[HomeKitの言及方法](/jp/design/human-interface-guidelines/homekit#Referring-to-HomeKit)を参照してください。

**アプリのデータベースがHomeKitのものと異なる場合はHomeKitに従う。** ユーザ体験がシームレスなものになるように、ホームアプリやその他のHomeKit対応の他社製アプリでの変更が自動的に反映されるようにします。ユーザにアプリで設定の競合を解消してもらう必要がある場合は、その競合を視覚的に示して、何の選択を求められているのかをユーザが明確に把握できるようにしてください。例えば、ホームアプリ内でアクセサリのサービス名が変更された場合、アプリでこの変更を検出したら、ユーザに変更前と変更後のサービス名を並べて示し、変更後のサービス名をあなたのアプリ内でも使用するかどうかを確認できます。

**アプリ内での変更をHomeKitデータベースに反映する場合はユーザに許可を取る。** ホームアプリを変更することにより、ユーザが驚かないようにしましょう。そのためには、データベースに書き込む前にユーザの許可を取るか、書き込む旨を伝えることが重要です。特に、ユーザからの明示的な指示なしにHomeKitデータベースの設定を書き換えることはしないでください。

### [カメラ](/jp/design/human-interface-guidelines/homekit#Cameras)

HomeKitに対応したネットワーク接続型IPカメラからの静止画像やストリーミング動画をアプリに表示できます。

**カメラの映像を妨げない。** 何らかの異変に注意を向けるような通知など、カメラの映像を補足する便利な機能を追加するのはかまいません。ただし、ほかのコンテンツによってカメラの映像が部分的にでも隠れてしまうことがないようにしましょう。

**マイクボタンはカメラが双方向オーディオに対応している場合にのみ表示する。** マイクが使えないのにマイクボタンを表示しても、アプリの貴重なスペースを奪うだけです。また、ユーザの混乱も招きかねません。

## [HomeKitアイコンを使用する](/jp/design/human-interface-guidelines/homekit#Using-HomeKit-icons)

HomeKitアイコンは、HomeKitテクノロジーに関する設定や説明を伝える場合に使用します。

![HomeKitアイコン。](https://docs-assets.developer.apple.com/published/926a46dc1cdf9647a94303a329c43645/homekit-glyph%402x.png)

また、Apple Homeアプリに言及する場合や、App StoreでApple Homeの[プロダクトページ](https://itunes.apple.com/us/app/home/id1110145103?mt=8)を開くボタンでは、Apple Homeアプリのアイコンを使用できます。

![Apple Homeアプリのアイコン。屋根の右側に煙突の付いた記号化された家が、オレンジのグラデーションで描かれています。](https://docs-assets.developer.apple.com/published/2dd7e937870e9cde3c818264d031e15c/homeapp-icon%402x.png)

**Appleが提供しているアイコンのみを使用する。** HomeKitやホームアプリのアイコンデザインを自作したり、Appleが提供しているデザインを真似しようとしたりしないでください。HomeKitアイコンは[リソース](https://developer.apple.com/design/resources/)からダウンロードできます。

### [スタイル](/jp/design/human-interface-guidelines/homekit#Styles)

HomeKitアイコンの表示スタイルには複数の選択肢があります。

#### [黒いHomeKitアイコン](/jp/design/human-interface-guidelines/homekit#Black-HomeKit-icon)

ほかのテクノロジーアイコンも黒で表示される場合は、白または明るい背景上のHomeKitアイコンを使用します。

![黒い輪郭線のHomeKitアイコン。](https://docs-assets.developer.apple.com/published/739a8ed96d427f7a1e8eb680feab203c/homekit-black-icon-set%402x.png)

#### [白いHomeKitアイコン](/jp/design/human-interface-guidelines/homekit#White-HomeKit-icon)

ほかのテクノロジーアイコンも白で表示される場合は、黒または暗い背景上のHomeKitアイコンを使用します。

![白い輪郭線のHomeKitアイコン。](https://docs-assets.developer.apple.com/published/86f0a2b6f128e579b0b2400f3e8c7fa7/homekit-white-icon-set%402x.png)

#### [カスタムカラーのHomeKitアイコン](/jp/design/human-interface-guidelines/homekit#Custom-color-HomeKit-icon)

ほかのテクノロジーアイコンがカスタムカラーで表示される場合は、同じカラーを使用します。

![青い輪郭線のHomeKitアイコン。](https://docs-assets.developer.apple.com/published/f7e6e6aaf077dbcb7cba53cbadf8436d/homekit-custom-color-icon-set%402x.png)

**HomeKitアイコンの配置をほかのテクノロジーアイコンと一致させる。** ほかのテクノロジーアイコンをシェイプの中に表示する場合は、HomeKitアイコンも同様に表示します。

![3つのアプリアイコンが横に並んでいる図。アイコンの上に「連係」というテキストがあります。左端のアプリアイコンは円に囲まれたHomeKitアイコンで、下に「Apple HomeKit」というテキストがあります。ほかの2つのアプリアイコンは、円の中にある点線の正方形で、下に「テクノロジー」というテキストがあります。](https://docs-assets.developer.apple.com/published/d99dcb889282d5caec808ff2c666db92/homekit-settings%402x.png)

**HomeKitアイコンをインタラクティブなものにしない。** カスタムのインタラクティブな要素やボタンにHomeKitアイコンや _HomeKit_ という名称を使用しないでください。App Storeのプロダクトページを開く要素にApple Homeアプリのアイコンを使用することはできます。

![HomeKitアイコンの正しくない使い方の図。円形のボタンの中にアイコンがあり、全体にクロムめっきのスタイルが適用されてしまっています。](https://docs-assets.developer.apple.com/published/08c6b1888cd04ea864bfe8d037eb1814/homekit-donot1%402x.png)

![丸に囲まれた×印は不適切な使い方を示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![カスタムのグラデーション背景を持つボタンに、誤って「HomeKit」というタイトルが付けられてしまっている図。](https://docs-assets.developer.apple.com/published/0c8ae4ebd1f0d755d78391a46602eda0/homekit-donot2%402x.png)

![丸に囲まれた×印は不適切な使い方を示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

**HomeKitアイコンをテキストの中やHomeKitという語の代わりに使用しない。** テキスト内でのHomeKitの適切な言及方法については、[HomeKitの言及方法](/jp/design/human-interface-guidelines/homekit#Referring-to-HomeKit)を参照してください。

![テキスト内でのHomeKitアイコンの使い方の例を示す一連の画像の1つ目。この正しい例では行頭にアイコンがあり、その後ろに「HomeKitで設定された照明」というテキストが続いています。](https://docs-assets.developer.apple.com/published/d6048913e65fd5d9d388a2092b1fa60d/homekit-lights-right%402x.png)

![丸に囲まれたチェックマークは正しい使い方を示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![テキスト内でのHomeKitアイコンの使い方の例を示す一連の画像の2つ目。この例では「HomeKitで設定された照明」というテキストの「HomeKit」の後ろに誤ってアイコンが配置されてしまっています。](https://docs-assets.developer.apple.com/published/c1b83e63c29a6036e1bf6d2103d75f1a/homekit-lights-wrong1%402x.png)

![丸に囲まれた×印は不適切な使い方を示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![テキスト内でのHomeKitアイコンの使い方の例を示す一連の画像の3つ目。この例では「で設定された照明」というテキストの行頭に誤ってアイコンが配置されてしまっています。](https://docs-assets.developer.apple.com/published/3ee27c477e85deb75431a4bface755c2/homekit-lights-wrong2%402x.png)

![丸に囲まれた×印は不適切な使い方を示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

**アイコンと _HomeKit_ という名称を正しく対にする。**ほかのテクノロジーについてもアイコンの横または下に名称を表示する場合は、HomeKitも同様に表示してかまいません。フォントはレイアウト内のほかの部分と同じものを使用してください。関連するガイダンスは、[HomeKitの言及方法](/jp/design/human-interface-guidelines/homekit#Referring-to-HomeKit)を参照してください。

![設定情報を含むアプリ内ビューの図。ビューの一番上には「設定」というタイトルがあり、その下に区切り線があります。区切り線の下には、アイコン、テキスト、その他の情報を表示するための開閉用矢印ボタンからなる行が3行あります。1行目には、HomeKitアイコンに続いて「HomeKit」という語が表示されています。ほかの2行にはほかのアプリアイコンを表す点線の正方形があり、それぞれのアイコンに続いて「名前」というテキストが表示されています。](https://docs-assets.developer.apple.com/published/2f3912a46b148cc8e0b37d4b7a803c6d/homekit-setup%402x.png)設定または説明コンテンツでアプリと名称を使用する方法

![4つのアプリボタンのグリッドを含むビューの図。ビューの一番上には「アプリ」というタイトルがあり、その下に区切り線があります。区切り線の下には、ボタンとラベルを2つずつ含む段が2段表示されています。1段目の1つ目のボタンにはApple Homeアプリのアイコンがあり、その下に「Apple Home」というテキストが表示されています。ほかのボタンにはほかのアプリアイコンを表す点線の正方形があり、それぞれのアイコンの下に「アプリ名」というテキストが表示されています。](https://docs-assets.developer.apple.com/published/2d78f370246fb95ddcf9b2be5513494d/homekit-apps%402x.png)アイコンと名称でApple Homeアプリに言及する方法

## [HomeKitの言及方法](/jp/design/human-interface-guidelines/homekit#Referring-to-HomeKit)

**HomeKitよりもアプリの方を強調する。** HomeKitやApple Homeがあなたのアプリの名前やメインアイデンティティよりも目立たないようにします。

**Appleの商標ガイドラインに従う。** アプリの名前や画像の中でAppleの商標を使用することは禁止されています。テキスト内では、Appleの製品名は[Apple商標リスト](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html)の記載に厳密に従って使用します。

  * Appleの製品名は単数形でのみ使用する。Appleの製品名を所有格にしない。

  * Apple、Apple Home、HomeKit、その他のAppleの商標を翻訳しない。

  * カテゴリ名を使用しない。例えば、タブレットではなくiPadと呼びます。

  * Appleからのいかなるスポンサーシップ、パートナーシップ、またはエンドースメントも示唆しない。

  * 法的情報が表示されるアプリ内の場所では、必ず、Apple、HomeKit、その他のAppleの商標に正しいクレジット表記を付ける。

  * Appleのデバイスおよびオペレーティングシステムへの言及は、技術仕様または互換性の説明内にのみとどめる。

| テキストの例  
---|---  
![丸に囲まれたチェックマークは正しい使い方を示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| HomeKitを使うとiPhoneまたはiPadから照明を点けることができます。  
![丸に囲まれた×印は不適切な使い方を示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)| HomeKitを使うとiOSデバイスから照明を点けることができます。  
  
[Apple商標および著作権使用に関するガイドライン](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)を参照してください。

### [HomeKitおよびホームアプリへの言及](/jp/design/human-interface-guidelines/homekit#Referencing-HomeKit-and-the-Home-app)

** _HomeKit_ という用語を使うときは大文字と小文字を正しく使用する。** _HomeKit_ は1つの単語からなり、大文字の _H_ と大文字の _K_ の後ろは小文字です。 _Apple Home_ は2つの単語からなり、大文字の _A_ と大文字の _H_ の後ろは小文字です。名称がすべて大文字で表示されるレイアウトでは、周囲のスタイルに合わせて _HomeKit_ または _Apple Home_ をすべて大文字で表示してかまいません。

** _HomeKit_ を修飾語として使用しない。**代わりに、「 _と連係する_ 」「 _を使用する_ 」「 _に対応している_ 」「 _と互換性がある_ 」といった語句と共に使用します。

| テキストの例  
---|---  
![丸に囲まれたチェックマークは正しい使い方を示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| [ブランド名]電球はHomeKitと連係します。  
![丸に囲まれたチェックマークは正しい使い方を示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| HomeKit対応のサーモスタット  
![丸に囲まれたチェックマークは正しい使い方を示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| [アプリ名]ではHomeKitを使用できます。  
![丸に囲まれた×印は不適切な使い方を示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)| HomeKit電球。  
  
**HomeKitがアクションや機能を実行しているかのような書き方をしない。**

|  テキストの例  
---|---  
![丸に囲まれたチェックマークは正しい使い方を示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| HomeKitによって裏口が施錠されました。  
![丸に囲まれた×印は不適切な使い方を示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)| HomeKitが裏口を施錠しました。  
  
**必要に応じて _HomeKit_ に _Apple_ を付ける。**

| テキストの例  
---|---  
![丸に囲まれたチェックマークは正しい使い方を示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| Apple HomeKitと互換性があります。  
  
**必要に応じて「設定」「構成」「説明」に _HomeKit_ という名称を使用する。**

| テキストの例  
---|---  
![丸に囲まれたチェックマークは正しい使い方を示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| HomeKitの設定を開きます。  
  
** _Apple Home_ に言及する場合は必ずそのアプリ名を使用する。**本文でのアプリ名の初出時には、 _Apple Home_ というフルネームを使用します。その後はホームアプリと書いてかまいません。

| テキストの例  
---|---  
![丸に囲まれたチェックマークは正しい使い方を示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| Apple Homeアプリを開きます。  
![丸に囲まれたチェックマークは正しい使い方を示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| Apple Homeアプリを開きます。これで、アクセサリと部屋がホームアプリに表示されるようになります。  
![丸に囲まれた×印は不適切な使い方を示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)| ホームを開きます。  
  
## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/homekit#Platform-considerations)

 _iOS、iPadOS、macOS、tvOS、visionOS、watchOSに追加の考慮事項はありません。_

## [リソース](/jp/design/human-interface-guidelines/homekit#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/homekit#Related)

[Appleデザインリソース](https://developer.apple.com/design/resources/)

[Apple商標および著作権使用に関するガイドライン](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/homekit#Developer-documentation)

[HomeKit](/documentation/HomeKit)

#### [ビデオ](/jp/design/human-interface-guidelines/homekit#Videos)

[](https://developer.apple.com/videos/play/wwdc2021/10298)

## [変更履歴](/jp/design/human-interface-guidelines/homekit#Change-log)

日付| 変更内容  
---|---  
2023年5月02日| ガイダンスを1ページに統合しました。
