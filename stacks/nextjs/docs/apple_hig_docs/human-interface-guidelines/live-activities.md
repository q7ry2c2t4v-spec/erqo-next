# ライブアクティビティ

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/live-activities

2025年12月16日

すべてのプラットフォームのガイダンスを更新、およびmacOSとCarPlayのガイダンスを追加。 

# ライブアクティビティ

ライブアクティビティでは、ユーザがアクティビティ、イベント、またはタスクの進行状況を一目でトラッキングできます。

![折りたたまれた状態と展開された状態の、スポーツ中継のスコアを表示している図案化されたDynamic Island。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/0f299ec4d1f667d200694c1080ef1498/components-live-activities-intro%402x.png)

ライブアクティビティを使用すると、ユーザがどのデバイスでも一目でわかる場所でタスクやイベントをトラッキングし続けることができます。 プッシュ通知よりも高機能で、数時間にわたってコンテンツやステータスのアップデートを頻繁に提供し、ユーザが表示される情報を操作できるようにします。

例えば、フードデリバリーの注文が到着するまでの残り時間、サッカーの試合のライブの試合情報、またはリアルタイムのフィットネス指標やワークアウトを一時停止またはキャンセルするインタラクティブなコントロールを表示できます。

ライブアクティビティは、iPhoneまたはiPadで開始されると、ユーザのデバイスのシステムの場所に自動的に表示されます。

プラットフォームまたはシステム操作| 場所  
---|---  
iPhoneおよびiPad| ロック画面、ホーム画面、iPhoneのDynamic Islandおよび「スタンバイ」  
Mac| メニューバー  
Apple Watch| スマートスタック  
CarPlay| CarPlayダッシュボード  
  
## [構造](/jp/design/human-interface-guidelines/live-activities#Anatomy)

ライブアクティビティは、 _Dynamic Island_ やロック画面など、システム全体のさまざまな場所に表示されます。これは、進行中のアクティビティの通知とインジケータの統合ホームとしての役割を果たします。デバイスとライブアクティビティが表示されるシステムの場所に応じて、ライブアクティビティの見た目を構成する _表示_ スタイルやスタイルの組み合わせが選択されます。そのため、ライブアクティビティは以下に対応する必要があります:

  * [コンパクト](/jp/design/human-interface-guidelines/live-activities#Compact)

  * [最小限](/jp/design/human-interface-guidelines/live-activities#Minimal)

  * [拡張](/jp/design/human-interface-guidelines/live-activities#Expanded)

  * [ロック画面](/jp/design/human-interface-guidelines/live-activities#Lock-Screen)

iOSおよびiPadOSのライブアクティビティは、これらの表示を使ってシステム全体にわたって表示されます。また、ほかのコンテキストのデフォルトの見た目も、これらを使って作成されます。例えば、コンパクト表示はiPhoneのDynamic Islandに表示され、2つの要素で構成されます。Apple WatchとCarPlayでは、この2つの要素が1つのビューに結合されます。

### [コンパクト](/jp/design/human-interface-guidelines/live-activities#Compact)

Dynamic Islandでは、アクティブなライブアクティビティが1つしかない場合にコンパクト表示が使用されます。この表示は、TrueDepthカメラの先頭側と末尾側という、2つに分かれた要素で構成されます。スペースは限られていますが、コンパクト表示はアプリのライブアクティビティに関する最新情報を表示します。

![Dynamic Islandのコンパクトな先頭側ビューとコンパクトな末尾側ビューを示す図。](https://docs-assets.developer.apple.com/published/409abb0732bda36b7064f8f8c9631407/type-compact%402x.png)

デザインのガイダンスは、[コンパクト表示](/jp/design/human-interface-guidelines/live-activities#Compact-presentation)を参照してください。

### [最小限](/jp/design/human-interface-guidelines/live-activities#Minimal)

複数のライブアクティビティがアクティブな場合は、最小限の表示が使用されてDynamic Islandにそのうち2つが表示されます。一方はDynamic Islandに結合され、他方は切り離されて表示されます。切り離された最小限の表示は、コンテンツのサイズに応じて円形または楕円形で表示されます。コンパクト表示の場合と同様に、ユーザが最小限の表示をタップするとアプリが開き、タッチして押さえたままにすると拡張表示されます。

![Dynamic Islandの最小限の表示を示す図。](https://docs-assets.developer.apple.com/published/a03ac6fcba9f6f89d180c0a4c745a755/type-minimal%402x.png)

デザインのガイダンスは、[最小限の表示](/jp/design/human-interface-guidelines/live-activities#Minimal-presentation)を参照してください。

### [拡張](/jp/design/human-interface-guidelines/live-activities#Expanded)

コンパクトまたは最小限の表示のライブアクティビティを長押しすると、拡張表示されます。

![Dynamic Islandの拡張ビューを示す図。](https://docs-assets.developer.apple.com/published/4e5af6b7073ffa8245e0efd5e6815f0d/type-expanded%402x.png)

デザインのガイダンスは、[拡張表示](/jp/design/human-interface-guidelines/live-activities#Expanded-presentation)を参照してください。

### [ロック画面](/jp/design/human-interface-guidelines/live-activities#Lock-Screen)

システムはロック画面表示を使用してロック画面下部にバナーを表示します。この表示では拡張表示に似たレイアウトを使用してください。

![Dynamic Islandに対応しているiPhoneのロック画面に表示されたライブアクティビティのスクリーンショット。](https://docs-assets.developer.apple.com/published/d6a5d144a2dea3d76a2ff56d6bac2c2a/live-activity-lock-screen%402x.png)

Dynamic Islandに対応していないデバイスでライブアクティビティのアップデートについて通知すると、ロック画面表示がバナーとしてホーム画面やほかのアプリの上に短時間表示されます。

![Dynamic Islandに対応していないiPhoneのホーム画面にバナーとして表示されたライブアクティビティのスクリーンショット。](https://docs-assets.developer.apple.com/published/e1c9f57eb05ab51dd4673e1c17d88847/live-activity-notch%402x.png)

デザインのガイダンスは、[ロック画面表示](/jp/design/human-interface-guidelines/live-activities#Lock-Screen-presentation)を参照してください。

### [スタンバイ](/jp/design/human-interface-guidelines/live-activities#StandBy)

「スタンバイ」のiPhoneでは、ライブアクティビティは最小限の表示で表示されます。これをタップすると、ロック画面表示に変化し、2倍に拡大されて画面いっぱいに表示されます。ロック画面表示でカスタムのバックグラウンドカラーを使っている場合は、画面全体に自動的に拡大され、シームレスなフルスクリーンデザインが生成されます。

![「スタンバイ」で2倍に拡大されたライブアクティビティがロック画面表示されている画像。点線はライブアクティビティを2倍に拡大した大きさを示しています。](https://docs-assets.developer.apple.com/published/155406263525b44222c63bfda84fa402/live-activity-standby-default-outline%402x.png)

デザインのガイダンスは、[スタンバイ表示](/jp/design/human-interface-guidelines/live-activities#StandBy-presentation)を参照してください。

## [ベストプラクティス](/jp/design/human-interface-guidelines/live-activities#Best-practices)

**開始と終了が定義されているタスクやイベントについてのライブアクティビティを提供する。** ライブアクティビティは、8時間を超えない短時間から中程度の時間のアクティビティのトラッキングに最適です。

**ユーザが一目で確認する必要がある重要な情報に的を絞る。** ライブアクティビティにあらゆる情報を表示する必要はありません。ユーザにとって最も役立つ情報は何かを考え、それを簡潔に伝えることを優先します。さらに詳しく知りたい場合、ユーザはライブアクティビティをタップして、追加情報を提供できるアプリを開くことができます。

**ライブアクティビティを使って広告やプロモーションを表示しない。** ライブアクティビティは、進行中のイベントやタスクについてユーザが常に情報を入手できるようにするものであるため、それらのイベントやタスクに関連する情報のみを表示することが重要です。

**機密情報を表示しないようにする。** ライブアクティビティは視覚的に目立つため、ロック画面や常時表示ディスプレイなどを何気なく見たほかの人に見られてしまう可能性があります。機密情報や個人情報とユーザに受け取られる可能性があるコンテンツの場合は、当たり障りのない概要を表示し、ライブアクティビティがタップされたときにアプリで機密情報を表示するようにしてください。または、機密情報を含む可能性があるビューを隠すか、機密データを表示するかどうかをユーザが設定できるようにします。デベロッパ向けのガイダンスは、[ウィジェット機能拡張の作成](/documentation/WidgetKit/Creating-a-Widget-Extension#Hide-sensitive-content)を参照してください。

**アプリのデザインや特徴に一致したライブアクティビティを作成し、ダークとライトの両方に対応する。** これにより、ユーザがライブアクティビティを認識しやすくなり、アプリとの視覚的なつながりが生まれます。

**ロゴマークを含める場合はコンテナなしで表示する。** これにより、ロゴマークとライブアクティビティのレイアウトの一体感が強まります。アプリアイコン全体を使わないようにしてください。

**Dynamic Islandに注目させる要素をアプリに追加しない。** ライブアクティビティがDynamic Islandに表示されるのは、アプリが使われていないときです。また、アプリが開いているときには、別の項目がDynamic Islandに表示される可能性があります。

**テキストを読みやすくする。** 太さ中以上の大きく太いテキストを使用します。小さなテキストの使用は控えめにして、重要な情報が一目で読めるようにします。

![小さくて読みにくいDynamic Islandのテキストを示す図。](https://docs-assets.developer.apple.com/published/84236e9e77ed0e5bfa06925a904fa7f0/live-activities-text-incorrect-size%402x.png)

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![太くて判読可能なサイズのDynamic Islandのテキストを示す図。](https://docs-assets.developer.apple.com/published/e7b78ebd2b48a88350938c0022c540a6/live-activities-text-correct-size%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

### [ライブアクティビティのレイアウト作成](/jp/design/human-interface-guidelines/live-activities#Creating-Live-Activity-layouts)

**異なる画面サイズおよび表示に適応する。** ライブアクティビティはさまざまなデバイスの画面に収まるように拡大/縮小されます。画面上での実際のサイズは異なる場合や変化する場合があることを認識して、さまざまなデバイスおよび拡大率に適したレイアウトや素材を作成してください。[仕様](/jp/design/human-interface-guidelines/live-activities#Specifications)に示されている値を目安として使用し、適切なサイズのコンテンツを提供して、どこでも見栄えよく表示されるようにしてください。

**スペースを効率よく使うため、要素のサイズと配置を調整する。** 必要以上のスペースを使わないレイアウトを作成して、コンテンツを明確に表示します。うまく収まるように、ライブアクティビティの要素のサイズと配置を調整します。

**カスタムのビューやレイアウトには使い慣れたレイアウトを使う。**[Appleデザインリソース](https://developer.apple.com/design/resources/)には、デフォルトのシステムマージンや推奨されるテキストサイズが使われているテンプレートが用意されています。これを使うことで、ライブアクティビティが一目で判読できる状態を維持しつつ、Apple Watchのスマートスタックなどの周囲のデザインと調和させることができます。

![均等なマージンが設けられたDynamic Islandのコンテンツの図。](https://docs-assets.developer.apple.com/published/10fc82dca81754b7f02dd13991469cfe/live-activities-margins%402x.png)

**一定のマージンを使い、同心円状に配置する。** 四隅など、丸みを帯びた図形とライブアクティビティの端の間には均等で適切なマージンを設け、調和のとれた配置にします。これにより、要素がライブアクティビティの丸みを帯びた図形に突き刺さるのを防ぎ、視覚的な緊張感をなくすことができます。例えば、ライブアクティビティの端近くに角丸四角形を配置する場合は、マージンを差し引き、SwiftUIコンテナを使用して正確な半径を適用することで、要素の角の半径をライブアクティビティの外側の角の半径に合わせます。デベロッパ向けのガイダンスは、[`ContainerRelativeShape`](/documentation/SwiftUI/ContainerRelativeShape)を参照してください。

![ライブアクティビティの図。Dynamic Islandの端にコンテンツが描画されています。](https://docs-assets.developer.apple.com/published/881638db784a565ec2af57941e8dec5d/live-activities-rounded-shapes%402x.png)

ライブアクティビティの外縁と同心円状のマージン内にコンテンツをコンパクトに収めてください。

![アイコンを含むライブアクティビティの図。アイコンはDynamic Islandの端から離れすぎています。](https://docs-assets.developer.apple.com/published/c8d09b063d4302302fe0241fa891df95/live-activities-content-incorrect-position%402x.png)

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![アイコンを含むライブアクティビティの図。アイコンはDynamic Islandの端のそばにあり、Dynamic Islandの丸みを帯びた図形とは重なっていません。](https://docs-assets.developer.apple.com/published/5313ebec022e7120eca90a99a94256d4/live-activities-content-correct-position%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

**コンテンツのブロックを分割するときは、コンテナ図形の中にはめ込むか、太い線を使う。** Dynamic Islandの端近くまでコンテンツを描画しないようにします。

![コンテンツを分割するため、Dynamic Islandの端近くまでコンテンツを描画する様子を示したライブアクティビティの図。](https://docs-assets.developer.apple.com/published/a07493ff41a19357dc1695f1b58745f3/live-activities-separating-content-incorrect%402x.png)

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![ライブアクティビティの図。丸みを帯びた図形の中にコンテンツを配置し、グループ化しています。](https://docs-assets.developer.apple.com/published/f14d90f0c93a0b59e51dbd0de00d24a7/live-activities-separating-content-pill%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![ライブアクティビティの図。線を使ってコンテンツのブロックを分けています。](https://docs-assets.developer.apple.com/published/e98c01f5edfba4c4c1d722f1ee3a7076/live-activities-separating-content-separator%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

ヒント

ライブアクティビティビューの丸みのある角に丸みのないコンテンツを配置する場合は、描画ツールで丸みのないコンテンツをぼかすとよいかもしれません。コンテンツをぼかすと、ビューの外側の境界にそろえやすくなることがあります。

![ぼかされたテキストを含むライブアクティビティの図。テキストはDynamic Islandの端から離れすぎています。](https://docs-assets.developer.apple.com/published/4f43ee56b07ee1ec7abe6478200c09f0/live-activities-blur-content-incorrect-position%402x.png)

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![ぼかされたテキストを含むライブアクティビティの図。テキストはDynamic Islandの端のそばにあり、Dynamic Islandの丸みを帯びた図形とは重なっていません。](https://docs-assets.developer.apple.com/published/38d008fbd8930a26c9fcd34136f2b9b1/live-activities-blur-content-correct-position%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

**ロック画面や拡張表示のライブアクティビティの高さを動的に変える。** 表示する情報が少ない場合は、ライブアクティビティの高さを減らして、コンテンツに必要なだけのスペースを使うようにします。多くの情報が利用できるようになったら、高さを増やして、追加コンテンツを表示します。例えば、配車サービスアプリでは、運転手を探している間は詳細情報のないコンパクトなライブアクティビティを表示できます。詳しい情報が入手できるようになったら、アプリの高さを追加して、到着見込み時間や運転手の詳細などを表示します。

### [カラーを選ぶ](/jp/design/human-interface-guidelines/live-activities#Choosing-colors)

**カスタムのバックグラウンドカラーや不透明度を使用する場合は慎重に検討する。** コンパクト表示、最小限の表示、および拡張表示のバックグラウンドカラーはカスタマイズできません。ただし、ロック画面表示では、カスタムのバックグラウンドカラーを使用できます。ロック画面表示でカスタムのバックグラウンドカラーや背景画像を設定する場合、特に輝度が下がった状態の常時表示ディスプレイを搭載したデバイスでの色合いでは、十分なコントラストを確保してください。

**アプリの特徴や個性を表現するカラーを使う。** Dynamic Islandのライブアクティビティには、不透明な黒いバックグラウンドを使います。テキストやオブジェクトに大胆なカラーを使うことで、アプリの特徴やブランドを表現することを検討してください。大胆なカラーを使うことで、一目でライブアクティビティを認識できるようになり、ほかのライブアクティビティと見分けやすく、すぐに確認できる小さなアプリの一部のようになります。また、大胆なカラーを使うことで、ライブアクティビティ自体の要素の関連性が際立つようになります。

**ライブアクティビティのキーラインには、アプリのコンテンツと一致するカラーを使う。** 例えばダークモードなどでバックグラウンドが暗い場合は、Dynamic Islandの周囲にキーラインが表示され、ほかのコンテンツと区別されます。キーラインには、ライブアクティビティのほかの要素と一貫性のあるカラーを選びます。デベロッパ向けのガイダンスは、[ライブアクティビティのカスタムビューの作成](/documentation/ActivityKit/creating-custom-views-for-live-activities#Use-custom-colors)を参照してください。

### [トランジションの追加とコンテンツアップデートのアニメーション](/jp/design/human-interface-guidelines/live-activities#Adding-transitions-and-animating-content-updates)

ライブアクティビティでは、拡大や縮小のトランジションに加え、システムアニメーションやカスタムアニメーションが最大2秒間表示されます。輝度が下がった状態の常時表示ディスプレイではアニメーションは実行されません。

**アニメーションは、伝えたい情報を強調するためや、アップデートに注意を引くために使用する。** 要素の位置を移動させたり、デフォルトのコンテンツ置換トランジションを使って要素の出入りをアニメートさせたり、拡大縮小や不透明度、移動によるカスタムトランジションを作成したりできます。例えばスポーツアプリでは、数字コンテンツのトランジションを使ってスコアを変化させたり、タイマーがゼロになったときにフェードイン/アウトさせたりすることができます。

**アニメーションでレイアウトを変化させる。** 「スタンバイ」で画面いっぱいに拡大する場合や、詳しい情報が利用できるようになったときなど、コンテンツのアップデートによってライブアクティビティのレイアウトの変更が必要になる場合があります。新しいレイアウトにトランジションする際には、削除してからアニメーションで追加するのではなく、既存の要素を新しい位置にアニメーションさせることで、できる限り既存のレイアウトを維持します。

**要素の重なりを避ける。** トランジションのほかの部分とぶつかるのを避けるため、要素をアニメートアウトしてから新しい位置にアニメートインする方が望ましい場合もあります。例えば、リスト内で項目をアニメートする場合は、新しい位置に移動する要素のみをアニメートさせ、ほかのリスト項目にはフェードインまたはフェードアウトトランジションを使用します。

デベロッパ向けのガイダンスは、[ウィジェットとライブアクティビティのデータアップデートのアニメーション](/documentation/WidgetKit/Animating-data-updates-in-widgets-and-live-activities)を参照してください。

### [インタラクティブな操作の提供](/jp/design/human-interface-guidelines/live-activities#Offering-interactivity)

**ライブアクティビティがタップされたときにアプリの正しい場所が開くようにする。** ユーザが関連する情報を探すために移動しなくてもいいように、関連する詳細情報やアクションに直接遷移するようにします。特定の画面へのディープリンクに対応したSwiftUIビューのデベロッパ向けのガイダンスは、[ウィジェットまたはライブアクティビティからの特定のアプリのシーンへのリンク](/documentation/WidgetKit/Linking-to-specific-app-scenes-from-your-widget-or-Live-Activity)を参照してください。

**シンプルで直接的なアクションに的を絞る。** ボタンやトグルは有用な情報の表示スペースを占めることになります。インタラクティブな要素は、ライブアクティビティに直接関係する必要不可欠な機能で、ミュージックの再生、ワークアウト、またはマイクにアクセスしてライブオーディオを録音するアプリなど、1回だけ有効にしたり、一時的に停止と再開を切り替えたりするもののみ含めます。インタラクティブな機能を提供する場合は、ユーザが意図せずに誤ったコントロールをタップしてしまうことを防ぐため、1つの要素に限定します。

**ユーザがイベントや進行状況アップデートに反応できるようにすることを検討する。** ライブアクティビティのアップデートに対してユーザが反応できる場合は、ボタンやトグルを提供してユーザがアクションを実行できるようにすることを検討してください。例えば、配車サービスアプリのライブアクティビティに、到着を待っている間に運転手に連絡するためのボタンを含めることができます。

### [ライブアクティビティを開始、アップデート、終了する](/jp/design/human-interface-guidelines/live-activities#Starting-updating-and-ending-a-Live-Activity)

**ライブアクティビティは適切なタイミングで開始し、アプリで簡単にオフにできるようにする。** ユーザは、ライブアクティビティが開始され、すぐに、または特定の時間に、場合によっては自動的に、タスクの重要なアップデートが提供されることを期待します。例えば、食事の注文や配車サービスのリクエストのあと、またはお気に入りのチームの試合が始まったときに、ライブアクティビティが開始されると期待する場合があります。しかし、予期せず表示されるライブアクティビティには驚かされ、迷惑であることもあります。アクティビティに対応するアプリのビューで、ユーザがライブアクティビティをオフにするためのコントロールを提供することを検討してください。例えばスポーツアプリでは、試合やチームのフォローを解除するボタンを提供できます。ユーザがライブアクティビティの見た目をアプリから簡単に制御できない場合は、「設定」でライブアクティビティを完全にオフにしてしまう場合があります。

**ライブアクティビティを開始するアプリショートカットを提供する。** アプリショートカットは、機能をシステムに公開して、さまざまな状況からアクセスできるようにします。例えば、iPhoneのアクションボタンを使ってライブアクティビティを開始できるようにするアプリショートカットを作成します。詳しくは、[アプリショートカット](/jp/design/human-interface-guidelines/app-shortcuts)を参照してください。

**新しいコンテンツがあるときだけライブアクティビティをアップデートする。** 対象のコンテンツやステータスが変わらない場合は、そのコンテンツやステータスが変化するまで同じ表示を維持します。

**注目してもらう必要がある不可欠なアップデートのみ通知する。** ライブアクティビティの通知を行うと、ユーザがアップデートを見逃すことがないように、画面が点灯し、デフォルトで通知音が再生されます。また、通知はDynamic Islandで拡大表示され、Dynamic Islandに対応していないデバイスではバナーとして表示されます。ライブアクティビティで最大の価値を提供できるように、頻繁すぎる通知や重要でないアップデートの通知は避け、同じアップデートに対してライブアクティビティとプッシュ通知を併用しないでください。

**1つのライブアクティビティで複数のイベントを効率的にトラッキングできるようにする。** 複数のイベントをトラッキングする場合は、別々のライブアクティビティを作成してユーザに切り替えさせるのではなく、1つのライブアクティビティで動的なレイアウトを使用して、イベントを順番に表示できるようにします。例えばスポーツアプリでは、1つのライブアクティビティで複数の試合のスコア、選手交代、およびファウルを順番に表示することができます。

**ライブアクティビティは必ずタスクやイベントが終了したときに即座に終了するようにする。閉じるまでのカスタムの時間を設定することを検討する。** 終了したライブアクティビティは、Dynamic IslandとCarPlayからは即座に削除されます。ロック画面、Macのメニューバー、およびwatchOSのスマートスタックには、最大で4時間残ります。ライブアクティビティによっては、概要を表示しても、終了後のわずかな時間しか意味をなさない場合があります。ライブアクティビティの継続時間に応じて、閉じるまでのカスタムの時間を選択することを検討してください。ほとんどの場合は、15分から30分で十分でしょう。例えば、配車サービスアプリのライブアクティビティは、降車したタイミングで終了できます。ユーザが降車後何時間も配車情報を気にする可能性は低いので、30分だけ表示が残るようにします。デベロッパ向けのガイダンスは、[ライブアクティビティでのライブデータの表示](/documentation/ActivityKit/displaying-live-data-with-live-activities#End-the-Live-Activity)を参照してください。

## [表示](/jp/design/human-interface-guidelines/live-activities#Presentation)

ライブアクティビティは、あらゆる場所、デバイス、それに対応する見た目に適応できる必要があります。システムによって表示されるサイズが異なるため、それぞれの表示場所に最適なライブアクティビティのレイアウトを作成してください。

**iPhoneのデザインから始めたあと、ほかのコンテキストに合わせて微調整する。** まず、各表示の標準デザインを作成します。そのあと、ライブアクティビティで提供する機能に応じて、「スタンバイ」のiPhone、CarPlay、Apple Watchなどの特定のコンテキスト向けのカスタムレイアウトを追加でデザインします。カスタムレイアウトについて詳しくは、[スタンバイ](/jp/design/human-interface-guidelines/live-activities#StandBy)、[CarPlay](/jp/design/human-interface-guidelines/live-activities#CarPlay)、および[watchOS](/jp/design/human-interface-guidelines/live-activities#watchOS)を参照してください。

### [コンパクト表示](/jp/design/human-interface-guidelines/live-activities#Compact-presentation)

**最も重要な情報に的を絞る。** ライブアクティビティにとって必要不可欠な最新情報を動的に、かつわかりやすく表示する場合は、コンパクト表示を使用します。例えばスポーツアプリでは、2つのチームのロゴとスコアを表示します。

**Dynamic Island内のコンパクト表示の情報とデザインの統一性を確保する。** TrueDepthカメラによって先頭側と末尾側の要素が分けられていますが、それらを1つの情報として読めるようにデザインし、統一感のあるカラーや文字を使用して両方の要素のつながりを表現します。

**コンテンツはできる限りコンパクトにまとめ、TrueDepthカメラに対してきれいに収まるようにする。** ステータスバーの重要な情報を不明瞭にしたり、コンテンツとTrueDepthカメラの間にパディングを追加したりしないようにしてください。先頭側と末尾側の両方の要素に同じようなサイズのビューを表示して、バランスの取れたレイアウトを保ちます。例えば、短い単位や精度を下げたデータを使うことで、適切な幅やバランスを保ちます。

![TrueDepthカメラのまわりにパディングがあるため、広すぎてバランスが取れていない見た目になったコンパクト表示を示した図。](https://docs-assets.developer.apple.com/published/cf94bf048c32e220b373a7f1603b76b7/live-activities-unbalanced-content%402x.png)

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![TrueDepthカメラに対してきれいに収まっているコンパクト表示を示した図。](https://docs-assets.developer.apple.com/published/a90890fd165fcb8921cef4aaa4648427/live-activities-balanced-content%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

**関連するアプリのコンテンツにリンクする。** ユーザがコンパクトなライブアクティビティをタップしたときは、アプリの関連する詳細画面が直接開きます。先頭側と末尾側の両方の要素が同じ画面にリンクするようにしてください。

### [最小限の表示](/jp/design/human-interface-guidelines/live-activities#Minimal-presentation)

**最小限の表示でもライブアクティビティを認識できるようにする。** 可能な場合は、ロゴだけでなく最新情報を表示するようにします。ただし、ユーザがすぐにアプリを認識できるようにしてください。例えば、タイマーアプリのライブアクティビティの最小限の表示には、静的なアイコンではなく、残り時間が表示されます。

### [拡張表示](/jp/design/human-interface-guidelines/live-activities#Expanded-presentation)

**要素の相対的な配置を維持し、一貫性のあるレイアウトを作成する。** 拡張表示はコンパクト表示または最小限の表示を拡大したバージョンです。ライブアクティビティが拡大されたときに、情報やレイアウトが予想できる形で拡大されるようにしてください。

**コンテンツをTrueDepthカメラの近くで折り返す。** スペースを効率的に使い、カメラを目立ちにくくするため、TrueDepthカメラの近くにコンテンツを配置し、カメラの周辺に大きな余白が残らないようにします。

![拡張表示されたライブアクティビティの図。TrueDepthカメラの横に何もないスペースがあります。](https://docs-assets.developer.apple.com/published/a28d1a7e10913995ed8674567c73e144/live-activities-layout-incorrect%402x.png)

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![拡張表示されたライブアクティビティの図。TrueDepthカメラの横のスペースが活用されています。](https://docs-assets.developer.apple.com/published/807023f5ec76e4132b23f9fdfc274278/live-activities-layout-correct%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

### [ロック画面表示](/jp/design/human-interface-guidelines/live-activities#Lock-Screen-presentation)

**通知レイアウトを複製しない。** ライブアクティビティに表示する情報に固有な独自レイアウトを作成します。

**パーソナライズされたロック画面になじむカラーを選択する。** ユーザは、壁紙、カスタムのカラーの色合いやウィジェットでロック画面をカスタマイズします。文字の読みやすさを損なわずに、カスタマイズされたロック画面のデザインに合うようにするには、ライブアクティビティに適度にカスタムの背景または色合いと不透明度を使用します。

**ダークモードと常時表示ディスプレイで、デザイン、アセット、カラーが見栄えよく十分なコントラストが確保されるようにする。** デフォルトでは、ロック画面のライブアクティビティには、明るい背景のときに明るいバックグラウンドカラーが使われ、暗い背景のときに暗いバックグラウンドカラーが使われます。カスタムのバックグラウンドカラーを使用する場合は、両方のモードに対応できるカラーを選ぶか、それぞれの見た目で別のカラーを選びます。常時表示ディスプレイでは必要に応じてカラーが調整されるので、輝度が下がった状態でのデバイスで確認するようにしてください。ガイダンスは[ダークモード](/jp/design/human-interface-guidelines/dark-mode)および[常時表示](/jp/design/human-interface-guidelines/always-on)を参照してください。デベロッパ向けのガイダンスは、[アセットカタログについて](https://help.apple.com/xcode/mac/current/#/dev10510b1f7)を参照してください。

**生成された閉じるボタンのカラーを確認する。** 閉じるボタンは、ライブアクティビティのバックグラウンドカラーとフォアグラウンドカラーに基づいて自動生成されます。 生成されたカラーがデザインと一致することを確認し、必要に応じて[`activitySystemActionForegroundColor(_:)`](/documentation/SwiftUI/View/activitySystemActionForegroundColor\(_:\))を使って調整します。

**標準のマージンを使ってデザインを通知に合わせる。** ロック画面のライブアクティビティでは、標準のレイアウトのマージンは14ポイントです。グラフィックスやボタンなどの要素には狭いマージンの方がよい場合もありますが、端までコンテンツが詰まって窮屈な見た目にならないようにしてください。デベロッパ向けのガイダンスは、[`padding(_:_:)`](/documentation/SwiftUI/View/padding\(_:_:\))を参照してください。

### [スタンバイ表示](/jp/design/human-interface-guidelines/live-activities#StandBy-presentation)

**「スタンバイ」用にレイアウトをアップデートする。** 拡大されたときでもアセットの見栄えがよくなるようにしてください。また、追加スペースを活用するカスタムレイアウトを作成することを検討してください。デベロッパ向けのガイダンスは、[ライブアクティビティのカスタムビューの作成](/documentation/ActivityKit/creating-custom-views-for-live-activities)を参照してください。

**「スタンバイ」ではデフォルトのバックグラウンドカラーを使用することを検討する。** デフォルトのバックグラウンドカラーでは、ライブアクティビティとデバイスのベゼルがシームレスにブレンドされ、ユーザの環境とやわらかく融合しているように見えます。また、TrueDepthカメラの周囲のマージンを考慮する必要がないため、ライブアクティビティをわずかに大きくすることができます。

**標準のマージンを使用し、グラフィックス要素が画面の端に重ならないようにする。** 標準のマージンがないと、ライブアクティビティが拡大したときにコンテンツが切れて表示されるので、壊れているように見えます。

**ナイトモードでデザインを確認する。** ナイトモードでは、ライブアクティビティに赤い淡色表示が適用されます。ライブアクティビティのデザインに使うカラーが、ナイトモードで十分なコントラストを持つことを確認してください。

![iPhoneの「スタンバイ」で、画面全体を覆うように拡大されたライブアクティビティ。](https://docs-assets.developer.apple.com/published/ca6f9f881d38d0678426975451fda3f0/live-activity-standby-night-mode%402x.png)

## [CarPlay](/jp/design/human-interface-guidelines/live-activities#CarPlay)

CarPlayでは、コンパクト表示の先頭側と末尾側の要素が、CarPlayダッシュボードに表示される1つのレイアウトに自動的に結合されます。

ライブアクティビティのデザインはCarPlayとApple Watchの両方に適用されるので、両方のコンテキスト向けにデザインします。Apple Watchのライブアクティビティはインタラクティブにすることができますが、CarPlayではインタラクティブ要素は無効になります。詳しくは、下の[watchOS](/jp/design/human-interface-guidelines/live-activities#watchOS)を参照してください。デベロッパ向けのガイダンスは、[ライブアクティビティのカスタムビューの作成](/documentation/ActivityKit/creating-custom-views-for-live-activities)を参照してください。

**ライブアクティビティのテキストを大きくしたり、追加情報を含めたりすることが有用な場合は、カスタムレイアウトの作成を検討する。** CarPlayのデフォルトの見た目を使うのではなく、[`ActivityFamily.small`](/documentation/WidgetKit/ActivityFamily/small)補助アクティビティファミリーに対応することを宣言します。

**カスタムレイアウトにボタンやトグルを含める場合は慎重に検討する。** CarPlayでは、ライブアクティビティのインタラクティブ要素は無効になります。ユーザが運転中にライブアクティビティを開始したりチェックしたりしそうな場合は、ボタンやトグルではなく、タイムリーなコンテンツを表示するようにしてください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/live-activities#Platform-considerations)

 _iOS、iPadOSに追加の考慮事項はありません。tvOSとvisionOSには対応していません。_

### [macOS](/jp/design/human-interface-guidelines/live-activities#macOS)

アクティブなライブアクティビティは、ペアリングされているMacのメニューバーに、自動的にコンパクト表示、最小限の表示、および拡張表示で表示されます。ライブアクティビティをクリックすると、iPhoneミラーリングが起動してアプリが表示されます。

### [watchOS](/jp/design/human-interface-guidelines/live-activities#watchOS)

iPhoneでライブアクティビティが開始されると、ペアリングされているApple Watchのスマートスタックの一番上に表示されます。デフォルトでは、iPhoneのライブアクティビティのコンパクト表示に表示される先頭と末尾の要素が組み合わされてスマートスタックに表示されます。

watchOSアプリを提供している場合に、ユーザがスマートスタックでライブアクティビティをタップすると、そのwatchOSアプリが開きます。watchOSアプリがない場合、タップするとフルスクリーン表示が開き、そこにあるボタンをタップすると、ペアリングされているiPhoneのアプリが開きます。

**カスタムのwatchOSレイアウトの作成を検討する。** デフォルトのビューが自動的に提供されますが、Apple Watch向けにカスタムレイアウトをデザインすると、さらに情報を表示して、ボタンやトグルなどのインタラクティブな機能を追加することができます。

**カスタムレイアウトにボタンやトグルを含める場合は慎重に検討する。** カスタムのwatchOSレイアウトは、CarPlayのライブアクティビティにも適用されますが、インタラクティブ要素は無効になります。ユーザが運転中にライブアクティビティを開始したりチェックしたりしそうな場合は、カスタムのwatchOSレイアウトにボタンやトグルを含めないでください。デベロッパ向けのガイダンスは、[ライブアクティビティのカスタムビューの作成](/documentation/ActivityKit/creating-custom-views-for-live-activities)を参照してください。

![iPhoneのDynamic Islandに表示されるライブアクティビティのコンパクト表示を示す図。](https://docs-assets.developer.apple.com/published/fe40353408dc5dc8e44405874bebc500/live-activities-ios-dynamic-island-default%402x.png)iPhoneのコンパクト表示

![自動的に生成されたライブアクティビティのデフォルト表示がスマートスタックに表示されている図。iPhoneのコンパクト表示の先頭と末尾の要素が下部の両隅に分かれて表示されています。](https://docs-assets.developer.apple.com/published/c06e95cce887c9dfc9cd89787afcd80d/live-activity-watch-default-implementation%402x.png)デフォルトのスマートスタック表示

![ライブアクティビティのカスタム表示がスマートスタックに表示されている図。バランスのよいデザインに、カウントダウンタイマーのグラフィックス表示と説明テキストが表示されています。](https://docs-assets.developer.apple.com/published/153e0ac0cfcace25dc6f268f334fed90/live-activity-watch-custom-implementation%402x.png)カスタムのスマートスタック表示

**必要不可欠な情報と重要なアップデートに的を絞る。** スマートスタックのスペースをできる限り効率的に使い、ライブアクティビティで伝えられる最も有益な情報を考えてください。

  * 進行状況（配達予定時刻など）

  * ストップウォッチやタイマーのコントロールなどのインタラクティブ要素

  * スポーツのスコアの変化など、重要なアップデート

## [仕様](/jp/design/human-interface-guidelines/live-activities#Specifications)

ライブアクティビティをデザインする目安として、以下の値を使ってください。

### [CarPlayのサイズ](/jp/design/human-interface-guidelines/live-activities#CarPlay-dimensions)

ライブアクティビティは、車の画面のサイズと解像度に合わせて拡大/縮小される場合があります。デザインの確認には、以下の一覧の値を使用してください:

ライブアクティビティのサイズ（pt）  
---  
240x78  
240x100  
170x78  
  
CarPlay Simulatorを使って以下のスマート画面表示サイズ調整用の構成で、デザインをテストしてください。これは、CarPlayの「設定」＞「表示」から利用できます。

構成| 解像度（pt）  
---|---  
ワイドスクリーン| 1920x720  
縦向き| 900x1200  
標準| 800x480  
  
### [iOSのサイズ](/jp/design/human-interface-guidelines/live-activities#iOS-dimensions)

次の表に示す値はすべてポイント単位です。

画面サイズ（縦向き）| コンパクト、先頭側| コンパクト、末尾側| 最小限（値を範囲で指定）| 拡張（値を範囲で指定）| ロック画面（高さを範囲で指定）  
---|---|---|---|---|---  
430x932| 62.33x36.67| 62.33x36.67| 36.67～45x36.67| 408x84～160| 408x84～160  
393x852| 52.33x36.67| 52.33x36.67| 36.67～45x36.67| 371x84～160| 371x84～160  
  
Dynamic Islandでは44ポイントのコーナー半径が使用され、角丸の形状がTrueDepthカメラに一致します。

表示のタイプ| デバイス| Dynamic Islandの幅（pt）  
---|---|---  
コンパクトまたは最小限| iPhone 17 Pro Max| 250  
| iPhone 17 Pro| 230  
| iPhone Air| 250  
| iPhone 17| 230  
| iPhone 16 Pro Max| 250  
| iPhone 16 Pro| 230  
| iPhone 16 Plus| 250  
| iPhone 16| 230  
| iPhone 15 Pro Max| 250  
| iPhone 15 Pro| 230  
| iPhone 15 Plus| 250  
| iPhone 15| 230  
| iPhone 14 Pro Max| 250  
| iPhone 14 Pro| 230  
拡張| iPhone 17 Pro Max| 408  
| iPhone 17 Pro| 371  
| iPhone Air| 408  
| iPhone 17| 371  
| iPhone 16 Pro Max| 408  
| iPhone 16 Pro| 371  
| iPhone 16 Plus| 408  
| iPhone 16| 371  
| iPhone 15 Pro Max| 408  
| iPhone 15 Pro| 371  
| iPhone 15 Plus| 408  
| iPhone 15| 371  
| iPhone 14 Pro Max| 408  
| iPhone 14 Pro| 371  
  
### [iPadOSのサイズ](/jp/design/human-interface-guidelines/live-activities#iPadOS-dimensions)

次の表に示す値はすべてポイント単位です。

画面サイズ（縦向き）| ロック画面（高さを範囲で指定）  
---|---  
1366x1024| 500x84～160  
1194x834| 425x84～160  
1012x834| 425x84～160  
1080x810| 425x84～160  
1024x768| 425x84～160  
  
### [macOSのサイズ](/jp/design/human-interface-guidelines/live-activities#macOS-dimensions)

提供されたiOSのサイズを使用します。

### [watchOSのサイズ](/jp/design/human-interface-guidelines/live-activities#watchOS-dimensions)

スマートスタックのライブアクティビティでは、watchOSウィジェットと同じサイズが使用されます。

Apple Watchのサイズ| スマートスタックのライブアクティビティのサイズ（pt）  
---|---  
40mm| 152x69.5  
41mm| 165x72.5  
44mm| 173x76.5  
45mm| 184x80.5  
49mm| 191x81.5  
  
## [リソース](/jp/design/human-interface-guidelines/live-activities#Resources)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/live-activities#Developer-documentation)

[ActivityKit](/documentation/ActivityKit)

[SwiftUI](/documentation/SwiftUI)

[WidgetKit](/documentation/WidgetKit)

[WidgetKit戦略の策定](/documentation/WidgetKit/Developing-a-WidgetKit-strategy) — WidgetKit

#### [ビデオ](/jp/design/human-interface-guidelines/live-activities#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/216)

[](https://developer.apple.com/videos/play/wwdc2025/278)

[](https://developer.apple.com/videos/play/wwdc2024/10098)

[](https://developer.apple.com/videos/play/wwdc2023/10194)

[](https://developer.apple.com/videos/play/wwdc2023/10184)

## [変更履歴](/jp/design/human-interface-guidelines/live-activities#Change-log)

日付| 変更内容  
---|---  
2025年12月16日| すべてのプラットフォームのガイダンスを更新、およびmacOSとCarPlayのガイダンスを追加。  
2024年6月10日| watchOSでのライブアクティビティに関するガイダンスを追加。  
2023年10月24日| ガイダンスを補足および更新し、新しいアートワークを追加。  
2023年6月05日| iOS 17およびiPadOS 17の機能を追加するためにガイダンスを更新。  
2022年11月03日| アートワークと仕様をアップデート。  
2022年9月23日| 新規ページ。
