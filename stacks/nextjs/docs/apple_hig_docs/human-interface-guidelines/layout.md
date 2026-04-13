# レイアウト

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/layout

# レイアウト

さまざまなコンテキストに適応する一貫したレイアウトを使用すると、アプリがより使いやすくなり、ユーザがお気に入りのアプリやゲームをどのデバイスでも楽しめるようになります。

![大きい長方形と、その中の左上4分の1の小さい長方形のスケッチ。ウインドウ内のユーザインターフェイス要素の位置を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる黄色になっています](https://docs-assets.developer.apple.com/published/1bd5e1a9793622fd1ec9e22472ba49d0/foundations-layout-intro%402x.png)

アプリのレイアウトは、ユーザがアプリを開いた瞬間からコンテンツを把握するのに役立ちます。ユーザは、コントロールとコンテンツの間に慣れ親しんだ関係があることで、アプリの機能を使いやすく探しやすくなると期待しています。この点を考慮してレイアウトをデザインすることで、プラットフォームでのアプリの使用感が親しみやすいものになります。

Appleは、Appleテクノロジーを組み込み、すべてのAppleプラットフォームで実行できるアプリやゲームの設計に役立つように、テンプレートやガイドなどのリソースを提供しています。[Appleデザインリソース](https://developer.apple.com/design/resources/)を参照してください。

## [ベストプラクティス](/jp/design/human-interface-guidelines/layout#Best-practices)

**関連のある項目をグループ分けして必要な情報を見つけやすくする。** 例えば、余白、背景の形状、カラー、マテリアル、区切り線を使って、要素同士を関連付けたり、情報を明確な領域に分けることをおすすめします。その際、コンテンツとコントロールが明確に区別されていることを確認してください。

**周りに十分なスペースを確保して重要な情報を見つけやすくする。** 最も重要な情報は早く見たいものです。些末な情報を詰め込んだために肝心の情報が埋もれてしまったということがないようにしましょう。副次的な情報は、ウインドウのほかの部分で確認できるようにするか、追加のビューに含めるようにしてください。

**コンテンツを画面またはウインドウいっぱいに拡張する。** バックグラウンドやフルスクリーンのアートワークがディスプレイの端まで拡張されていることを確認します。また、スクロール可能なレイアウトの場合は、デバイスの画面の下や左右まで続いていることを確認します。サイドバーやタブバーなどのコントロールやナビゲーションコンポーネントは、同じ平面ではなくコンテンツに重ねて表示されます。レイアウトではこの点を考慮することが重要です。

コンテンツがウインドウ全体に広がっていない場合は、背景拡張ビューを使用して、サイドバーやインスペクタの下など、コントロールレイヤーの後ろにコンテンツを表示します。デベロッパ向けのガイダンスは、[`backgroundExtensionEffect()`](/documentation/SwiftUI/View/backgroundExtensionEffect\(\))および[`UIBackgroundExtensionView`](/documentation/UIKit/UIBackgroundExtensionView)を参照してください。

![フルスクリーンのiPadアプリのスクリーンショット。先頭側にサイドバーが表示されています。コンテンツ領域の上半分は、富士山の写真でいっぱいになっています。写真は画面の上端に向けて徐々にぼかしがかかり、末尾側では写真の重なって浮かんでいるツールバー項目がグループ分けされています。写真とサイドバーが交わる部分では、画像が反転してぼかしがかかり、サイドバーの下から画面の下端まで伸びています。](https://docs-assets.developer.apple.com/published/361f574d1b17f22156efc79858bf86dc/layout-background-extention-view%402x.png)

## [視覚的階層](/jp/design/human-interface-guidelines/layout#Visual-hierarchy)

**コントロールとコンテンツを区別する。** Liquid Glassマテリアルを活用して、コントロールの明確な見た目をiOS、iPadOS、macOSで一貫したものにします。背景の代わりに、スクロールエッジエフェクトを使用して、コンテンツとコントロール領域の間の遷移を表現します。ガイダンスは、[スクロールビュー](/jp/design/human-interface-guidelines/scroll-views)を参照してください。

**相対的重要性を伝えるように項目を配置する。** 多くのユーザは、上から下、先頭側から末尾側というように、横書きの文章を読むときの順で項目を見ていくので、特に重要な項目は、ウインドウ、ディスプレイ、[視野](/jp/design/human-interface-guidelines/spatial-layout#Field-of-view)の左上付近に配置しておくと基本的にうまくいきます。言語によって読む方向が異なる点に注意し、[右から左](/jp/design/human-interface-guidelines/right-to-left)に記述する言語を考慮してデザインしてください。

**コンポーネント同士を位置合わせすることでスキャンを容易にし、構成や階層構造を分かりやすく伝える。** 位置を合わせるとアプリの表示内容がきれいに整理されるほか、スクロールしているときや目を動かしているときでもコンテンツを追いやすくなるため、より情報を見つけやすくなります。インデントと同様、位置合わせには、情報の階層構造が理解しやすくなるメリットもあります。

**現在見えているもの以外にもコンテンツがあることが分かるように段階的な表示を利用する。** 大きなコレクション内の全項目を一度に表示することができない場合などは、現在見えているもの以外にも項目があることを示す必要があります。プラットフォームによりますが、例えば[開閉コントロール](/jp/design/human-interface-guidelines/disclosure-controls)を使用したり、項目の一部が見えるようにしておけば、ビューのスクロールなどによってさらにコンテンツが現れることが伝わります。

**コントロールが使いやすくなるように、周囲に十分なスペースを確保し、論理的なセクションにグループ分けする。** 関係のないコントロール同士の距離が近すぎたり、ほかのコンテンツを周りに詰め込んだりすると、コントロールを区別したり機能を理解したりするのが難しくなることがあります。こうなると、アプリやゲームが使いにくくなってしまうかもしれません。ガイダンスは、[ツールバー](/jp/design/human-interface-guidelines/toolbars)を参照してください。

## [適応性](/jp/design/human-interface-guidelines/layout#Adaptability)

すべてのアプリやゲームは、デバイスやシステムのコンテキストが変化したときに適応する必要があります。iOS、iPadOS、tvOS、visionOSでは、アプリやゲームの見た目に影響することがあるデバイス環境の違いを特徴付ける、一連の _特性_ が定義されています。SwiftUIまたはAuto Layoutを使用すると、次のようなさまざまな特性やコンテキストの変化にインターフェイスを動的に適応させることができます。これらのツールを使わない場合は、別の方法を使ってこれを行う必要があります。

特に一般的で対処が必要になるデバイスとシステムのバリエーションには、以下のようなものがあります:

  * デバイスの複数の画面サイズ、解像度、色空間

  * デバイスの複数の向き（縦向き/横向き）

  * Dynamic Islandやカメラコントロールなどのシステム機能

  * iPadでの外部ディスプレイへの対応、拡大表示、サイズ変更可能なウインドウ

  * ダイナミックタイプでのテキストサイズの変化

  * 左から右/右から左のレイアウト方向、日付/時刻/数字フォーマット、フォントのバリエーション、テキストの長さなど、ロケールに応じた国際化機能

**認識の一貫性を保ちつつ、コンテキストの変更にうまく適応できるレイアウトをデザインする。** ユーザは、デバイスの回転、ウインドウのサイズ変更、ディスプレイの追加、デバイスの切り替えなどを行っても、問題なく機能して違和感を抱かせないアプリ体験を期待しています。システムで定義されているセーフエリア、マージン、ガイドを守り、レイアウトモディファイアでインターフェイス内のビューの配置を細かく調整すると、インターフェイスの適応性を確保するのに役立ちます。

**テキストサイズの変更に対応できるようにしておく。** ユーザは、異なるテキストサイズに対応できるアプリやゲームを高く評価します。iOS、iPadOS、tvOS、visionOS、watchOSでユーザが表示中のテキストのサイズを選択できる[ダイナミックタイプ](/jp/design/human-interface-guidelines/typography#Supporting-Dynamic-Type)に対応すると、ユーザがテキストのサイズを調整したときにアプリやゲームを適切に対応させることができます。Unityベースのゲームでダイナミックタイプに対応するには、Appleのアクセシビリティプラグインを使用します（デベロッパ向けのガイダンスは、[Apple – アクセシビリティ](https://github.com/apple/unityplugins/blob/main/plug-ins/Apple.Accessibility/Apple.Accessibility_Unity/Assets/Apple.Accessibility/Documentation~/Apple.Accessibility.md)を参照してください）。アプリ内でのテキストの表示についてのガイダンスは、[タイポグラフィ](/jp/design/human-interface-guidelines/typography)を参照してください。

**複数の向き、ローカリゼーション、テキストサイズを使って複数のデバイスでアプリをプレビューする。** さまざまな体験のうち、最大と最小のレイアウトを使用するものからテストを始めると、テストプロセスを合理化できます。一般的には広色域などの機能を実際のデバイスでプレビューすることが最善ですが、Xcode Simulatorを使ってクリッピングやその他のレイアウト上の問題を確認できます。例えば、横向きモードに対応しているiOSのアプリやゲームの場合、Simulatorを使って、デバイスが左右どちらに回転してもレイアウトが美しく表示されることを確認できます。

**必要な場合はディスプレイの変化に合わせてアートワークの倍率を変える。** 例えば、アプリやゲームを見るコンテキストが変わった場合（アスペクト比の異なる画面で開かれた場合など）は、アートワークが切り取られたり、レターボックスまたはピラーボックスで表示されたりすることがあります。その場合は、アートワークのアスペクト比は変更せず、代わりにアートワークを拡大/縮小して重要な視覚コンテンツが隠れないようにしてください。visionOSでは、ウインドウがZ軸方向に移動するときには自動的に[スケール](/jp/design/human-interface-guidelines/spatial-layout#Scale)が調整されます。

## [ガイドとセーフエリア](/jp/design/human-interface-guidelines/layout#Guides-and-safe-areas)

 _レイアウトガイド_ は、コンテンツを画面上に配置し、位置を揃え、スペースを調整することができる四角形の領域を定義するものです。システムには、定義済みのレイアウトガイドが含まれています。それらを使うと、コンテンツの周囲に標準のマージンを適用したり、テキストを読みやすくするために幅を制限したりすることが容易になります。また、カスタムレイアウトガイドを定義することもできます。デベロッパ向けのガイダンスは、[`UILayoutGuide`](/documentation/UIKit/UILayoutGuide)および[`NSLayoutGuide`](/documentation/AppKit/NSLayoutGuide)を参照してください。

 _セーフエリア_ は、ツールバー、タブバー、その他ウインドウで提供されるビューで覆われないディスプレイの領域を定義するものです。セーフエリアは、iPhoneのDynamic IslandやMacの一部の機種のカメラハウジングなど、デバイスのインタラクティブ機能や表示機能との干渉を回避するために欠かせません。デベロッパ向けのガイダンスは、[`SafeAreaRegions`](/documentation/SwiftUI/SafeAreaRegions)および[セーフエリアと相対的にコンテンツを配置する](/documentation/UIKit/positioning-content-relative-to-the-safe-area)を参照してください。

**各プラットフォームのディスプレイおよびシステムの主要な特徴に配慮する。** アプリやゲームがそのような特徴に対応していないと、プラットフォームになじまず、ユーザが使いづらいと感じることがあります。セーフエリアを使用すると、ディスプレイやシステムの特徴との干渉を避けるのに役立つだけでなく、バーなどのインタラクティブなコンポーネントを考慮に入れて、サイズ変更の際にコンテンツを動的に再配置することができます。

各プラットフォーム向けのガイドやセーフエリアが含まれるテンプレートについては、「[Appleデザインリソース](https://developer.apple.com/design/resources/)」を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/layout#Platform-considerations)

### [iOS](/jp/design/human-interface-guidelines/layout#iOS)

**なるべく縦向きと横向きの両方に対応する。** デバイスの向きが変わってもうまく動作するアプリやゲームは、高く評価されます。ただし、縦向きのみまたは横向きのみで実行する必要がある体験もあります。これに該当する場合、両方の向きを試して対応する向きを見つける操作は、ユーザに任せることができます。ユーザにデバイスを回転するよう伝える必要はありません。アプリやゲームが横向きのみに対応している場合、ユーザがデバイスを左右どちらに回転させてもアプリが同じように正常に動作することを確認しましょう。

**ゲームでは、フルブリードのインターフェイスを優先する。** 角丸半径、センサーハウジング、Dynamic Islandなどの機能に対応しつつ、画面いっぱいに美しいインターフェイスを提供するようにします。必要な場合は、レターボックスやピラーボックスでゲームを表示するオプションをプレイヤーに提供することを検討します。

**フルサイズ幅のボタンは避ける。** ボタンは、システム定義のマージンを尊重し、画面の端から離して配置すると、iOSらしくなります。フルサイズ幅のボタンを含める必要がある場合は、ハードウェアの曲線と調和し、隣接するセーフエリアと揃えるようにしてください。

**ステータスバーを非表示にするのはアプリの価値や体験が向上する場合のみにする。** ステータスバーにはユーザにとって有意義な情報が表示されます。また、占有している領域はほとんどのアプリで十分に活用できない領域であるため、通常は表示しておくことをおすすめします。例外は、ゲームプレイやメディアの視聴などの深い体験を提供しており、ステータスバーを非表示にするのが妥当である場合です。

### [iPadOS](/jp/design/human-interface-guidelines/layout#iPadOS)

macOSでのウインドウの動作と同じように、ウインドウのサイズを最小幅や最小高さにまで自由に変更することができます。レイアウトをデザインする際には、このサイズ変更の動作と、可能なウインドウサイズの全範囲を考慮することが重要です。ガイダンスは、[マルチタスク](/jp/design/human-interface-guidelines/multitasking#iPadOS)と[ウインドウ](/jp/design/human-interface-guidelines/windows#iPadOS)を参照してください。

**ユーザがウインドウのサイズを変更した場合、できるだけコンパクトビューへの切り替えを遅らせる。** 最初にフルスクリーンビュー用にデザインし、フルレイアウトが収まらなくなった場合にのみコンパクトビューに切り替えるようにします。これにより、できるだけ多くの状況でUIがより安定し、見慣れたものになります。[分割ビュー](/jp/design/human-interface-guidelines/split-views)などのより複雑なレイアウトの場合は、ビューが狭くなるにつれて、インスペクタなど3次の列を非表示にすることをおすすめします。

**一般的なシステムで提供されるサイズでレイアウトをテストし、遷移がスムーズになるようにする。** ウインドウコントロールには、ウインドウを画面の半分、3分の1、4分の1に配置するオプションが用意されています。そのため、さまざまなデバイスで、各サイズのレイアウトを確認することが重要です。ユーザがウインドウサイズを最小から最大まで調整する際の予期しないUIの変化を最小限に抑えるようにしてください。

**適応型ナビゲーションには変換可能なタブバーを検討する。** 多くのアプリでは、ナビゲーションにタブバーとサイドバーのいずれかを選択する必要はありません。その代わりに、両方を備えたタブバースタイルを採用できます。アプリは、まずサイドバーまたはタブバーのいずれか選択した方で起動しますが、ユーザはタップして切り替えることができます。ビューのサイズが変更されると、ビューの幅に合わせて表示スタイルも変更されます。ガイダンスは、[タブバー](/jp/design/human-interface-guidelines/tab-bars)を参照してください。デベロッパ向けのガイダンスは、[`sidebarAdaptable`](/documentation/SwiftUI/TabViewStyle/sidebarAdaptable)を参照してください。

### [macOS](/jp/design/human-interface-guidelines/layout#macOS)

**コントロールや重要な情報をウインドウの下部に配置することを避ける。** ユーザがウインドウを動かして、ウインドウの下端が画面の下端より下になることがよくあります。

**ウインドウ上端のカメラハウジングにコンテンツを表示しない。** デベロッパ向けのガイダンスは、[`NSPrefersDisplaySafeAreaCompatibilityMode`](/documentation/BundleResources/Information-Property-List/NSPrefersDisplaySafeAreaCompatibilityMode)を参照してください。

### [tvOS](/jp/design/human-interface-guidelines/layout#tvOS)

**さまざまなサイズのテレビに対応する。** Apple TVでは、iPhoneやiPadのようにレイアウトが画面のサイズに自動的に適応せず、どのディスプレイでもアプリやゲームの同じインターフェイスが表示されます。さまざまな画面サイズで美しく見えるように、レイアウトのデザインには細心の注意を払ってください。

**画面のセーフエリアに従う。** プライマリコンテンツは、画面の上端と下端から60ポイント、左端と右端から80ポイント離して配置します。画面の端に近いコンテンツは見づらく、古いテレビではオーバースキャンにより意図せず切れてしまうこともあります。このゾーンの外は、意図的に画面の外にはみ出させるコンテンツや要素を部分的に表示する場合にのみ使用してください。

![テレビの図。上下左右にセーフゾーンの枠線が表示されています。枠線の上下の幅は60ポイント、左右の幅は80ポイントです。](https://docs-assets.developer.apple.com/published/1be425edd08beb67cba3c1000983581f/visual-design-safe-zone%402x.png)

**フォーカス可能な要素間に適切なパディングを含める。** UIKitとフォーカスAPIを使用する場合、いずれかの要素にフォーカスが移動するとその要素が大きくなります。フォーカスが置かれたときに要素がどのように表示されるかを考慮に入れ、重要な情報に重ならないようにします。デベロッパ向けのガイダンスは、[Apple TVのフォーカス操作について](/documentation/UIKit/about-focus-interactions-for-apple-tv)を参照してください。

![縦長の網掛けの四角形を使用して、フォーカス可能な項目間のパディングを示している図。](https://docs-assets.developer.apple.com/published/1cfcdddb80150197945945a6884a9ade/visual-design-padding%402x.png)

#### [グリッド](/jp/design/human-interface-guidelines/layout#Grids)

以下のグリッドレイアウトを使用すると、閲覧体験を最適化することができます。フォーカスのない行や列の間に適切な間隔を設けて、項目にフォーカスが移動したときに重ならないようにしてください。

UIKitのコレクションビューのフローエレメントを使用すると、コンテンツの幅と間隔に基づいてグリッドの列数が自動的に決定されます。デベロッパ向けのガイダンスは、[`UICollectionViewFlowLayout`](/documentation/UIKit/UICollectionViewFlowLayout)を参照してください。

![メディア項目の2列のグリッドを表示しているApple TVの図。追加のメディア項目が画面の右端と下端に部分的に表示されています。](https://docs-assets.developer.apple.com/published/29cbd7ef913d834c991bd303816e410d/visual-design-grid-2-column%402x.png)

#### [2列のグリッド](/jp/design/human-interface-guidelines/layout#Two-column-grid)

属性| 値  
---|---  
フォーカスのないコンテンツの幅| 860 pt  
横方向の間隔| 40 pt  
縦方向の最小間隔| 100 pt  
  
![メディア項目の3列のグリッドを表示しているApple TVの図。追加のメディア項目が画面の右端と下端に部分的に表示されています。](https://docs-assets.developer.apple.com/published/efc27c2f40d150e6350f03d8709527d8/visual-design-grid-3-column%402x.png)

#### [3列のグリッド](/jp/design/human-interface-guidelines/layout#Three-column-grid)

属性| 値  
---|---  
フォーカスのないコンテンツの幅| 560 pt  
横方向の間隔| 40 pt  
縦方向の最小間隔| 100 pt  
  
![メディア項目の4列のグリッドを表示しているApple TVの図。追加の列と行が画面の右端に部分的に表示されています。](https://docs-assets.developer.apple.com/published/b02a182e769f7a89201719f46547dabf/visual-design-grid-4-column%402x.png)

#### [4列のグリッド](/jp/design/human-interface-guidelines/layout#Four-column-grid)

属性| 値  
---|---  
フォーカスのないコンテンツの幅| 410 pt  
横方向の間隔| 40 pt  
縦方向の最小間隔| 100 pt  
  
![メディア項目の5列のグリッドを表示しているApple TVの図。追加のメディア項目が画面の右端と下端に部分的に表示されています。](https://docs-assets.developer.apple.com/published/6eebe97a166aceb55ed18304ac46be8d/visual-design-grid-5-column%402x.png)

#### [5列のグリッド](/jp/design/human-interface-guidelines/layout#Five-column-grid)

属性| 値  
---|---  
フォーカスのないコンテンツの幅| 320 pt  
横方向の間隔| 40 pt  
縦方向の最小間隔| 100 pt  
  
![メディア項目の6列のグリッドを表示しているApple TVの図。追加のメディア項目が画面の右端と下端に部分的に表示されています。](https://docs-assets.developer.apple.com/published/a2a7efa8dc58b3615082ba7e62e81437/visual-design-grid-6-column%402x.png)

#### [6列のグリッド](/jp/design/human-interface-guidelines/layout#Six-column-grid)

属性| 値  
---|---  
フォーカスのないコンテンツの幅| 260 pt  
横方向の間隔| 40 pt  
縦方向の最小間隔| 100 pt  
  
![メディア項目の7列のグリッドを表示しているApple TVの図。追加の列と行が画面の右端に部分的に表示されています。](https://docs-assets.developer.apple.com/published/3e625b746a4a31f083020cfa91674bd6/visual-design-grid-7-column%402x.png)

#### [7列のグリッド](/jp/design/human-interface-guidelines/layout#Seven-column-grid)

属性| 値  
---|---  
フォーカスのないコンテンツの幅| 217 pt  
横方向の間隔| 40 pt  
縦方向の最小間隔| 100 pt  
  
![メディア項目の8列のグリッドを表示しているApple TVの図。追加のメディア項目が画面の右端と下端に部分的に表示されています。](https://docs-assets.developer.apple.com/published/71f872111291a6f1b465ddfd4f4dc246/visual-design-grid-8-column%402x.png)

#### [8列のグリッド](/jp/design/human-interface-guidelines/layout#Eight-column-grid)

属性| 値  
---|---  
フォーカスのないコンテンツの幅| 184 pt  
横方向の間隔| 40 pt  
縦方向の最小間隔| 100 pt  
  
![メディア項目の9列のグリッドを表示しているApple TVの図。](https://docs-assets.developer.apple.com/published/19125b211b45864b26f33d8f54a98a87/visual-design-grid-9-column%402x.png)

#### [9列のグリッド](/jp/design/human-interface-guidelines/layout#Nine-column-grid)

属性| 値  
---|---  
フォーカスのないコンテンツの幅| 160 pt  
横方向の間隔| 40 pt  
縦方向の最小間隔| 100 pt  
  
**タイトルがある行は縦方向の間隔を広げる。** いずれかの行にタイトルが含まれる場合は、フォーカスのない前の行の下端とタイトルの中央までの間隔を十分に取って、詰まりすぎないようにします。また、タイトルの下端から行内のフォーカスのない項目の上端までも間隔を開けます。

**間隔に一貫性を持たせる。** コンテンツの間隔に一貫性がないとグリッドらしく見えなくなり、スキャンしにくくなります。

**部分的に隠れているコンテンツが対称に見えるようにする。** 完全に表示されているコンテンツに注意が向かうように、画面の両端で画面外に部分的に隠れているコンテンツの表示部分を同じ幅にします。

### [visionOS](/jp/design/human-interface-guidelines/layout#visionOS)

以下は、馴染みのある使いやすい操作感をvisionOSのアプリやゲームで実現するための、ウインドウ内でのコンテンツのレイアウトに関するガイダンスです。空間内でのウインドウの表示方法に関するガイダンスや、visionOSアプリでの奥行き、スケール、視野の使い方のベストプラクティスについては、[空間レイアウト](/jp/design/human-interface-guidelines/spatial-layout)を参照してください。visionOSのウインドウコンポーネントについて詳しくは、[ウインドウ > visionOS](/jp/design/human-interface-guidelines/windows#visionOS)を参照してください。

備考

標準ウインドウのコンテンツに奥行きを追加すると、コンテンツがウインドウの境界を越えてZ軸方向に伸びます。Z軸方向に伸びすぎたコンテンツは、システムによって切り取られます。

**アプリやゲームで最も重要なコンテンツやコントロールをなるべく中央に配置する。** ウインドウが大きい場合は特に、ウインドウの中央付近にあるコンテンツの方が、ユーザにとって見つけやすく操作もしやすくなります。

**ウインドウのコンテンツが境界からはみ出さないようにする。** visionOSでは、ウインドウのXY平面の境界のすぐ外にウインドウコントロールが表示されます。例えば、「共有」メニューはウインドウの上に表示され、サイズ変更や移動を行ったり、ウインドウを閉じたりするためのコントロールはウインドウの下に表示されます。2Dや3Dのコンテンツがこれらの領域に重なっていると、特にウインドウの下に表示されるシステム定義のコントロールが使いにくくなってしまいます。

**ウインドウ内に置くのが適切でないコントロールを追加で表示する場合はオーナメントを使用する。** オーナメントを使うと、システム定義のコントロールに干渉せずにアプリコントロールとウインドウを視覚的に関連付けておくことができます。例えば、ウインドウのツールバーとタブバーはオーナメントとして表示されます。ガイダンスは[オーナメント](/jp/design/human-interface-guidelines/ornaments)を参照してください。

**ウインドウのインタラクティブなコンポーネントを簡単に注視できるようにする。** インタラクティブなコンポーネントを楽に目で見て判別できるようにし、かつ、システム定義のホバーエフェクトがほかのコンテンツにかからないようにするには、インタラクティブなコンポーネントの周りに十分なスペースを確保する必要があります。例えばボタンの場合は、中心間の距離が60ポイント以上になるように配置してください。ガイダンスは、[視線](/jp/design/human-interface-guidelines/eyes)、[空間レイアウト](/jp/design/human-interface-guidelines/spatial-layout)、[ボタン＞visionOS](/jp/design/human-interface-guidelines/buttons#visionOS)を参照してください。

### [watchOS](/jp/design/human-interface-guidelines/layout#watchOS)

**コンテンツが画面の一方の端から他方の端までいっぱいに広がるようにデザインする。** Apple Watchのベゼルは、コンテンツの周囲に視覚的なパディングを提供します。貴重なスペースを無駄にしないために、要素間のパディングを最小にすることを検討してください。

![Apple Watchのワークアウトアプリの図。ワークアウトのメインリストが表示されています。現在フォーカスがあるワークアウト項目が、使用可能な画面領域の幅いっぱいに広がっていることが示されています。](https://docs-assets.developer.apple.com/published/4545ae2a18c48d139fddba6ff70d27d9/layout-full-width%402x.png)

**インターフェイス内で3つまたは4つ以上のコントロールを並べて配置しない。** 一般的なルールとして、グリフを含むボタンの場合は4つ以上、テキストを含むボタンの場合は3つ以上を並べて表示しないでください。通常、テキストのボタンは画面の幅いっぱいに表示することが推奨されますが、画面のスクロールが必要にならない限り、短いテキストラベルの2つのボタンを横に並べてもよいでしょう。

![3行のテキストの下に2つのボタンが並んでいるApple Watch画面の図。](https://docs-assets.developer.apple.com/published/9511d1e5a946db2d7aca21bf2f7e8fa8/layout-controls%402x.png)

**ユーザがほかの人に見せたい場合に備えて、表示の自動回転に対応する。** ユーザが手首を返すと通常はその動きに反応してディスプレイがスリープ状態になりますが、コンテンツを自動回転させた方がよい場合もあります。例えば、装着している人が画像を友達に見せたり、QRコードをリーダーにかざしたりしたい場合などです。デベロッパ向けのガイダンスは、[`isAutorotating`](/documentation/WatchKit/WKExtension/isAutorotating)を参照してください。

## [仕様](/jp/design/human-interface-guidelines/layout#Specifications)

### [iOS、iPadOSデバイスの画面サイズ](/jp/design/human-interface-guidelines/layout#iOS-iPadOS-device-screen-dimensions)

モデル| サイズ（縦向き）  
---|---  
12.9インチiPad Pro| 1024x1366 pt（2048x2732 px @2x）  
11インチiPad Pro| 834x1194 pt（1668x2388 px @2x）  
10.5インチiPad Pro| 834x1194 pt（1668x2388 px @2x）  
9.7インチiPad Pro| 768x1024 pt（1536x2048 px @2x）  
13インチiPad Air| 1024x1366 pt（2048x2732 px @2x）  
11インチiPad Air| 820x1180 pt（1640x2360 px @2x）  
10.9インチiPad Air| 820x1180 pt（1640x2360 px @2x）  
10.5インチiPad Air| 834x1112 pt（1668x2224 px @2x）  
9.7インチiPad Air| 768x1024 pt（1536x2048 px @2x）  
11インチiPad| 820x1180 pt（1640x2360 px @2x）  
10.2インチiPad| 810x1080 pt（1620x2160 px @2x）  
9.7インチiPad| 768x1024 pt（1536x2048 px @2x）  
8.3インチiPad mini| 744x1133 pt（1488x2266 px @2x）  
7.9インチiPad mini| 768x1024 pt（1536x2048 px @2x）  
iPhone 17 Pro Max| 440x956 pt（1320x2868 px @3x）  
iPhone 17 Pro| 402x874 pt（1206x2622 px @3x）  
iPhone Air| 420x912 pt（1260x2736 px @3x）  
iPhone 17| 402x874 pt（1206x2622 px @3x）  
iPhone 16 Pro Max| 440x956 pt（1320x2868 px @3x）  
iPhone 16 Pro| 402x874 pt（1206x2622 px @3x）  
iPhone 16 Plus| 430x932 pt（1290x2796 px @3x）  
iPhone 16| 393x852 pt（1179x2556 px @3x）  
iPhone 16e| 390x844 pt（1170x2532 px @3x）  
iPhone 15 Pro Max| 430x932 pt（1290x2796 px @3x）  
iPhone 15 Pro| 393x852 pt（1179x2556 px @3x）  
iPhone 15 Plus| 430x932 pt（1290x2796 px @3x）  
iPhone 15| 393x852 pt（1179x2556 px @3x）  
iPhone 14 Pro Max| 430x932 pt（1290x2796 px @3x）  
iPhone 14 Pro| 393x852 pt（1179x2556 px @3x）  
iPhone 14 Plus| 428x926 pt（1284x2778 px @3x）  
iPhone 14| 390x844 pt（1170x2532 px @3x）  
iPhone 13 Pro Max| 428x926 pt（1284x2778 px @3x）  
iPhone 13 Pro| 390x844 pt（1170x2532 px @3x）  
iPhone 13| 390x844 pt（1170x2532 px @3x）  
iPhone 13 mini| 375x812 pt（1125x2436 px @3x）  
iPhone 12 Pro Max| 428x926 pt（1284x2778 px @3x）  
iPhone 12 Pro| 390x844 pt（1170x2532 px @3x）  
iPhone 12| 390x844 pt（1170x2532 px @3x）  
iPhone 12 mini| 375x812 pt（1125x2436 px @3x）  
iPhone 11 Pro Max| 414x896 pt（1242x2688 px @3x）  
iPhone 11 Pro| 375x812 pt（1125x2436 px @3x）  
iPhone 11| 414x896 pt（828x1792 px @2x）  
iPhone XS Max| 414x896 pt（1242x2688 px @3x）  
iPhone XS| 375x812 pt（1125x2436 px @3x）  
iPhone XR| 414x896 pt（828x1792 px @2x）  
iPhone X| 375x812 pt（1125x2436 px @3x）  
iPhone 8 Plus| 414x736 pt（1080x1920 px @3x）  
iPhone 8| 375x667 pt（750x1334 px @2x）  
iPhone 7 Plus| 414x736 pt（1080x1920 px @3x）  
iPhone 7| 375x667 pt（750x1334 px @2x）  
iPhone 6s Plus| 414x736 pt（1080x1920 px @3x）  
iPhone 6s| 375x667 pt（750x1334 px @2x）  
iPhone 6 Plus| 414x736 pt（1080x1920 px @3x）  
iPhone 6| 375x667 pt（750x1334 px @2x）  
4.7インチiPhone SE| 375x667 pt（750x1334 px @2x）  
4インチiPhone SE| 320x568 pt（640x1136 px @2x）  
iPod touch（第5世代以降）| 320x568 pt（640x1136 px @2x）  
  
注意

上の表の倍率はすべてUIKitでの倍率であり、ネイティブの倍率とは異なる場合があります。デベロッパ向けのガイダンスは、[`scale`](/documentation/UIKit/UIScreen/scale)および[`nativeScale`](/documentation/UIKit/UIScreen/nativeScale)を参照してください。

### [iOS、iPadOSデバイスのサイズクラス](/jp/design/human-interface-guidelines/layout#iOS-iPadOS-device-size-classes)

サイズクラスは、レギュラーまたはコンパクトのどちらかの値になります。 _レギュラー_ は大きな画面または横向きの画面のことを指し、 _コンパクト_ は小さな画面または縦向きの画面のことを指します。デベロッパ向けのガイダンスは、[`UserInterfaceSizeClass`](/documentation/SwiftUI/UserInterfaceSizeClass)を参照してください。

異なるデバイスにおけるフルスクリーン体験では、画面サイズに応じてサイズクラスのさまざまな組み合わせが適用されます。

モデル| 縦向き| 横向き  
---|---|---  
12.9インチiPad Pro| Regular Width、Regular Height| Regular Width、Regular Height  
11インチiPad Pro| Regular Width、Regular Height| Regular Width、Regular Height  
10.5インチiPad Pro| Regular Width、Regular Height| Regular Width、Regular Height  
13インチiPad Air| Regular Width、Regular Height| Regular Width、Regular Height  
11インチiPad Air| Regular Width、Regular Height| Regular Width、Regular Height  
11インチiPad| Regular Width、Regular Height| Regular Width、Regular Height  
9.7インチiPad| Regular Width、Regular Height| Regular Width、Regular Height  
7.9インチiPad mini| Regular Width、Regular Height| Regular Width、Regular Height  
iPhone 17 Pro Max| Compact Width、Regular Height| Regular Width、Compact Height  
iPhone 17 Pro| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone Air| Compact Width、Regular Height| Regular Width、Compact Height  
iPhone 17| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone 16 Pro Max| Compact Width、Regular Height| Regular Width、Compact Height  
iPhone 16 Pro| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone 16 Plus| Compact Width、Regular Height| Regular Width、Compact Height  
iPhone 16| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone 16e| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone 15 Pro Max| Compact Width、Regular Height| Regular Width、Compact Height  
iPhone 15 Pro| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone 15 Plus| Compact Width、Regular Height| Regular Width、Compact Height  
iPhone 15| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone 14 Pro Max| Compact Width、Regular Height| Regular Width、Compact Height  
iPhone 14 Pro| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone 14 Plus| Compact Width、Regular Height| Regular Width、Compact Height  
iPhone 14| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone 13 Pro Max| Compact Width、Regular Height| Regular Width、Compact Height  
iPhone 13 Pro| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone 13| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone 13 mini| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone 12 Pro Max| Compact Width、Regular Height| Regular Width、Compact Height  
iPhone 12 Pro| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone 12| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone 12 mini| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone 11 Pro Max| Compact Width、Regular Height| Regular Width、Compact Height  
iPhone 11 Pro| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone 11| Compact Width、Regular Height| Regular Width、Compact Height  
iPhone XS Max| Compact Width、Regular Height| Regular Width、Compact Height  
iPhone XS| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone XR| Compact Width、Regular Height| Regular Width、Compact Height  
iPhone X| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone 8 Plus| Compact Width、Regular Height| Regular Width、Compact Height  
iPhone 8| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone 7 Plus| Compact Width、Regular Height| Regular Width、Compact Height  
iPhone 7| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone 6s Plus| Compact Width、Regular Height| Regular Width、Compact Height  
iPhone 6s| Compact Width、Regular Height| Compact Width、Compact Height  
iPhone SE| Compact Width、Regular Height| Compact Width、Compact Height  
iPod touch（第5世代以降）| Compact Width、Regular Height| Compact Width、Compact Height  
  
### [watchOSデバイスの画面サイズ](/jp/design/human-interface-guidelines/layout#watchOS-device-screen-dimensions)

Series| サイズ| 幅（ピクセル）| 高さ（ピクセル）  
---|---|---|---  
Apple Watch Ultra（第3世代）| 49mm| 422| 514  
10、11| 42mm| 374| 446  
10、11| 46mm| 416| 496  
Apple Watch Ultra（第1世代および第2世代）| 49mm| 410| 502  
7、8、9| 41mm| 352| 430  
7、8、9| 45mm| 396| 484  
4、5、6、およびSE（全世代）| 40mm| 324| 394  
4、5、6、およびSE（全世代）| 44mm| 368| 448  
1、2、3| 38mm| 272| 340  
1、2、3| 42mm| 312| 390  
  
## [リソース](/jp/design/human-interface-guidelines/layout#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/layout#Related)

[右から左](/jp/design/human-interface-guidelines/right-to-left)

[空間レイアウト](/jp/design/human-interface-guidelines/spatial-layout)

[レイアウトと編成](/jp/design/human-interface-guidelines/layout-and-organization)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/layout#Developer-documentation)

[SwiftUIによるカスタムレイアウトの作成](/documentation/SwiftUI/composing-custom-layouts-with-swiftui) — SwiftUI

#### [ビデオ](/jp/design/human-interface-guidelines/layout#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/356)

[](https://developer.apple.com/videos/play/wwdc2022/10056)

[](https://developer.apple.com/videos/play/wwdc2017/802)

## [変更履歴](/jp/design/human-interface-guidelines/layout#Change-log)

日付| 変更内容  
---|---  
2025年9月09日| iPhone 17、iPhone Air、iPhone 17 Pro、iPhone 17 Pro Max、Apple Watch SE 3、Apple Watch Series 11、およびApple Watch Ultra 3の仕様を追加。  
2025年6月09日| Liquid Glassに関するガイダンスを追加。  
2025年3月07日| iPhone 16e、11インチiPad、11インチiPad Air、13インチiPad Airの仕様を追加。  
2024年9月09日| iPhone 16、iPhone 16 Plus、iPhone 16 Pro、iPhone 16 Pro Max、およびApple Watch Series 10の仕様を追加。  
2024年6月10日| 軽微な修正を行い、構成を更新。  
2024年2月02日| iPadOSアプリのレイアウトでシステムコントロール領域を避けることに関するガイダンスを改善し、10.9インチiPad Airおよび8.3インチiPad miniの仕様を追加。  
2023年12月05日| visionOSウインドウのコンテンツを中央に配置するためのガイダンスを明確化。  
2023年9月15日| iPhone 15 Pro Max、iPhone 15 Pro、iPhone 15 Plus、iPhone 15、Apple Watch Ultra 2、およびApple Watch SEの仕様を追加。  
2023年6月21日| visionOSのガイダンスを追加するために更新。  
2022年9月14日| iPhone 14 Pro Max、iPhone 14 Pro、iPhone 14 Plus、iPhone 14、Apple Watch Ultraの仕様を追加。
