# マップ

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/maps

# マップ

マップを使うと、アプリやWebサイトに屋外または屋内の地理データを表示できます。

![3つ折りのマップのスケッチ。ナビゲーションを示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる青色になっています。](https://docs-assets.developer.apple.com/published/beaca39e9d51b0917123cf6bb204b940/technologies-maps-intro%402x.png)

マップでは、システムが提供するマップアプリとほぼ同じ機能（拡大/縮小、パン、回転など）に対応する、使い慣れたインターフェイスを提供します。マップには注釈やオーバーレイを含めたり、経路情報を表示したりできます。また、マップを構成して標準的なグラフィック表示にしたり、衛星写真ベースの表示にしたり、両方を使ってハイブリッド表示にしたりすることもできます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/maps#Best-practices)

**基本的にインタラクティブなマップにする。** ユーザは拡大/縮小やパンなど、使い慣れた方法でマップを操作できることを期待しています。インタラクティブではない要素でマップを隠してしまうと、マップの動作に対するユーザの期待に反してしまう場合があります。

**アプリのニーズに合わせてマップの強調スタイルを選ぶ。** 2つの強調スタイルから選ぶことができます。

  *  _デフォルト_ スタイルは、鮮明なカラーでマップを表示するバージョンで、カスタム要素をあまり使用しないほとんどの標準的なマップアプリに適したオプションです。このスタイルは、作成するマップの見た目を標準のマップアプリと合わせるときにも便利で、2つのアプリを行き来するような状況に適しています。

  * 一方、 _ミュート_ スタイルは、カラーの鮮やかさが抑えられたバージョンを表示します。このスタイルは、情報が豊富なコンテンツが数多くあり、マップに対して目立たせて表示したい場合に最適です。

![iPhoneのマップのスクリーンショット。デフォルトの強調スタイルでコイトタワーが表示されています。](https://docs-assets.developer.apple.com/published/603ad0c458f464ad072a94aa10ee89bb/maps-default-appearance%402x.png)

デフォルトのスタイル

![iPhoneのマップのスクリーンショット。淡色でコイトタワーが表示されています。これは控えめな強調スタイルを表しています。](https://docs-assets.developer.apple.com/published/31d94cbb32ab028e061cfff44b8e7c6a/maps-muted-appearance%402x.png)

控えめなスタイル

デベロッパ向けのガイダンスは、[`MKStandardMapConfiguration.EmphasisStyle`](/documentation/MapKit/MKStandardMapConfiguration/EmphasisStyle-swift.enum)を参照してください。

**マップで場所を見つけやすくする。** 検索機能を提供し、さらにカテゴリで場所を絞り込めるようにすることを検討してください。例えばショッピングモールのマップの検索フィールドでは、ファッション、インテリア、電化製品、アクセサリ、おもちゃなど、一般的なカテゴリの店舗を簡単に見つけられるフィルタを含めるとよいでしょう。

**ユーザが選択した要素を明確にする。** ユーザがマップ上で特定の領域やその他の要素を選択した場合は、枠などの特徴のあるスタイルを適用したりカラーを変えたりして、選択部分に注意を向けます。

**見どころが重なる場合はクラスタにまとめてマップを見やすくする。** _クラスタ_ は、1つのピンを使って周辺にある複数の見どころを表すものです。ユーザがマップを拡大すると、クラスタが展開されて個々の見どころが徐々に表示されていきます。

![3という数字が表示された1本のピンのスクリーンショット。近隣の3つの見どころが含まれるクラスタを表しています。](https://docs-assets.developer.apple.com/published/26a4541efb07044a1fa8f7a06cd0551c/maps-points-of-interest-cluster%402x.png)クラスタ内の見どころ

![拡大したときの3本のオレンジ色のピンのスクリーンショット。3つの個々の見どころを表しています。](https://docs-assets.developer.apple.com/published/c5c116cc73f331ef0e39b8ecb79a0984/maps-points-of-interest-individual%402x.png)拡大したときの個々の見どころ

**ユーザがAppleロゴや権利表示のリンクを見ることができるようにする。** ロゴやリンクが一時的にインターフェイスの一部に隠れてしまうのは問題ありませんが、これらの要素が常時隠れることがないようにしてください。以下のガイドラインに従い、Appleロゴと権利表示のリンクを常に表示してください。

  * 適切なパディングを使用して、ロゴとリンクをマップの境界線とカスタムコントロールから離します。例えば、要素の左右には7ポイントの、上下には10ポイントのパディングを使用するとうまく表示されます。

  * ロゴとリンクがインターフェイスと一緒に動かないようにします。Appleロゴと権利表示のリンクがマップに固定表示されるのが理想的です。

  * カスタムインターフェイスをマップと連動して動かせる場合は、カスタム要素の一番低い位置を基にロゴとリンクの配置を決めてください。例えば、画面の下部からカスタムカードを上に引いて開くことができるアプリでは、Appleロゴと権利表示のリンクを、カードが停止する一番下の位置から10ポイント上の場所に配置します。

注意

Appleロゴと権利表示のリンクは、200x100ピクセル未満のマップには表示されません。

## [カスタム情報](/jp/design/human-interface-guidelines/maps#Custom-information)

**アプリの見た目のスタイルに合った注釈を使う。** 注釈はマップ上のカスタムの見どころを示すマーカーです。デフォルトの注釈マーカーは、赤いカラーに白いピンのあるアイコンとして表示されます。カラーはアプリのカラースキームに合わせて変更できます。アイコンを文字列や、ロゴなどの画像に変更することもできます。文字列アイコンには、Unicode文字を含む、任意の文字を含めることができますが、読みやすいように2～3文字に留めてください。デベロッパ向けのガイダンスは、[`MKAnnotationView`](/documentation/MapKit/MKAnnotationView)を参照してください。

**標準のマップ機能に関連するカスタム情報を表示する場合は、個別に選択できるようにすることを検討する。** 選択可能なマップ機能に対応すると、システムでは、Appleが提供する要素（見どころ、国や都市名、地形要素など）が、デベロッパが追加したその他の注釈とは分けて扱われます。ユーザがこれらの要素を選択したときに、カスタムの見た目やカスタム情報で表すように構成することができます。デベロッパ向けのガイダンスは、[`MKMapFeatureOptions`](/documentation/MapKit/MKMapFeatureOptions)を参照してください。

**オーバーレイを使ってコンテンツに直接関係するマップ領域を定義する。**

  *  _道路の上_ はデフォルトのレベルで、オーバーレイは道路の上に配置されますが、建物や木などの要素の下になります。オーバーレイの下に何があるのかをユーザが分かるようにしながら、定義された領域がはっきりと理解できるようにする場合に最適です。

  *  _ラベルの上_ の場合、オーバーレイが道路とラベルの両方の上に配置され、その下にある要素がすべて隠れます。コンテンツをマップの要素から完全に引き離したい場合や、マップの中で関係のない領域を隠したい場合に便利です。

デベロッパ向けのガイダンスは、[マップへのオーバーレイの表示](/documentation/MapKit/displaying-overlays-on-a-map)および[`MKOverlayLevel`](/documentation/MapKit/MKOverlayLevel)を参照してください。

**カスタムコントロールとマップに十分なコントラストを持たせる。** コントラストが十分でないとコントロールが見にくくなり、マップに溶け込んでしまう可能性があります。細いストロークや薄いドロップシャドウを使ってカスタムコントロールを目立たせるか、マップ領域にブレンドモードを適用して、マップ上でのコントロールのコントラストを高めることを検討してください。

## [場所カード](/jp/design/human-interface-guidelines/maps#Place-cards)

場所カードは、アプリまたはWebサイトで、営業時間、電話番号、住所などの詳細な場所情報を表示します。これにより、指定場所の最新情報を整理して表示することで、検索結果を充実させることができます。

### [マップへの場所カードの表示](/jp/design/human-interface-guidelines/maps#Displaying-place-cards-in-a-map)

場所が選択されたときに、マップに直接場所カードを表示できます。ある著者がサイン会で訪問予定になっている書店のマップなど、複数の場所を指定できるマップで場所情報を表示したい場合は、この方法がおすすめです。デベロッパ向けのガイダンスは、[`mapItemDetailSelectionAccessory(_:)`](/documentation/MapKit/MapContent/mapItemDetailSelectionAccessory\(_:\))、[`mapView(_:selectionAccessoryFor:)`](/documentation/MapKit/MKMapViewDelegate/mapView\(_:selectionAccessoryFor:\))および[`selectionAccessory`](/documentation/MapKitJS/Annotation/selectionAccessory)を参照してください。

見どころ、領域、自然の地形など、マップのその他の場所の場所カードも表示することができます。これにより、近隣の場所についての貴重な情報を提供できます。デベロッパ向けのガイダンスは、[`mapFeatureSelectionAccessory(_:)`](/documentation/SwiftUI/View/mapFeatureSelectionAccessory\(_:\))、[`mapView(_:selectionAccessoryFor:)`](/documentation/MapKit/MKMapViewDelegate/mapView\(_:selectionAccessoryFor:\))および[`selectableMapFeatureSelectionAccessory`](/documentation/MapKitJS/Map/selectableMapFeatureSelectionAccessory)を参照してください。

デベロッパ向けの備考

Webサイトには、デフォルトで1か所の指定場所の場所カードを表示するカスタムマップを埋め込むことができます。デベロッパ向けのガイダンスは、[Maps Embed APIを使用した場所情報の表示](/documentation/MapKitJS/displaying-place-information-using-the-maps-embed-api)を参照してください。

システムでは、複数の場所カードのスタイルが定義されており、サイズ、見た目、場所カードに含める情報を指定できます。

  *  _自動_ スタイルを使用すると、システムが地図表示のサイズに基づいて場所カードのスタイルを決定します。

  *  _コールアウト_ スタイルでは、場所カードが選択した場所の横にポップオーバースタイルで表示されます。さらにコールアウトのスタイルを指定することもできます。 _フル_ コールアウトスタイルでは大きな詳細場所カードが、 _コンパクト_ コールアウトスタイルでは場所をとらない簡潔な場所カードが表示されます。コールアウトスタイルを指定しない場合、システムのデフォルトは _自動_ コールアウトスタイルになり、地図表示のサイズに基づいてコールアウトスタイルが決まります。

  *  _キャプション_ スタイルでは、「“マップ”で開く」リンクが表示されます。

  *  _シート_ スタイルでは、場所カードが[シート](https://developer.apple.com/jp/design/human-interface-guidelines/sheets)で表示されます。

デベロッパ向けのガイダンスは、[`MapItemDetailSelectionAccessoryStyle`](/documentation/MapKit/MapItemDetailSelectionAccessoryStyle)、[`MKSelectionAccessory.MapItemDetailPresentationStyle`](/documentation/MapKit/MKSelectionAccessory/MapItemDetailPresentationStyle)および[`PlaceSelectionAccessoryStyle`](/documentation/MapKitJS/PlaceSelectionAccessoryStyle)を参照してください。

![iPadのマップでのフルコールアウトスタイルの場所カードのスクリーンショット。場所カードの上部には、ヘッダ画像と場所の名前、カテゴリ、評価が表示されています。場所カードには、営業時間のタイル、Webサイト、電話番号、住所のタイル、「“マップ”で開く」リンクのタイルも含まれています。](https://docs-assets.developer.apple.com/published/c7ab22ffd9ad47e9499bd6bc68de1872/maps-place-card-ipad-full%402x.png)

![iPadのマップでのコンパクトコールアウトスタイルの場所カードのスクリーンショット。場所カードには、場所の名前、カテゴリ、短い住所、評価、「“マップ”で開く」リンクが表示されています。](https://docs-assets.developer.apple.com/published/7b345b93b076717f1e40e75575e49d75/maps-place-card-ipad-compact%402x.png)

![iPadのマップでのキャプションスタイルの場所カードのスクリーンショット。場所カードに「“マップ”で開く」リンクが表示されます。](https://docs-assets.developer.apple.com/published/b41cae51a4ce14ba5266d2e25660976f/maps-place-card-ipad-link%402x.png)

![iPadのマップでのシートスタイルの場所カードのスクリーンショット。地図表示の上に表示されます。場所カードの上部には、ヘッダ画像と場所の名前、カテゴリ、評価が表示されています。場所カードには、営業時間のタイル、Webサイト、電話番号、住所のタイル、「“マップ”で開く」リンクのタイルも含まれています。](https://docs-assets.developer.apple.com/published/c0949b0fa7cda4a313b15b5f8e658613/maps-place-card-ipad-sheet%402x.png)

フルコールアウトスタイルの場所カードは、デバイスによって表示が異なります。フルコールアウトスタイルの場所カードは、iPadOSとmacOSではポップオーバースタイルで、iOSでは[シート](https://developer.apple.com/jp/design/human-interface-guidelines/sheets)で表示されます。

![iPhoneのマップでのフルコールアウトスタイルの場所カードのスクリーンショット。場所カードは、シートとしてデバイスの下端から表示されます。](https://docs-assets.developer.apple.com/published/e79ad5fe1ee7e69e7134b6e5f7ec2623/maps-place-card-iphone-full%402x.png)

**マップの表示方法を考慮してスタイルを選ぶ。** フルコールアウトスタイルの場所カードでは、一番高度な体験が提供され、直接マップに表示できる場所情報の量が最も多くなります。ただし、マップのコンテキストに適した場所カードのスタイルを選ぶようにしてください。例えば、アプリでたくさんの注釈が付いた小さなマップを表示する場合は、コンパクトコールアウトスタイルを使い、マップのその他の指定場所のコンテキストを維持したまま、場所をとらずに場所情報を表示することを検討します。

**デバイスやウインドウサイズによらず、場所カードが見栄えよく表示されるようにする。** スタイルを指定する場合は、別のデバイスや異なるウインドウサイズでも、場所カードの内容が確実に表示されるようにします。フルコールアウトスタイルの場所カードでは、小さなデバイスでテキストがはみ出さないように、最低幅を設定できます。

**情報が重複しないようにする。** 場所カードのスタイルを選ぶときは、アプリやWebサイトにすでに表示した情報を考慮します。例えば、フルコールアウトスタイルの場所カードでは、アプリですでに表示した情報が表示される可能性があります。その場合は、コンパクトコールアウトまたはキャプションスタイルの方が適切かもしれません。

**場所カードを表示するときはマップの現在地を維持する。** こうすることで、詳しい場所情報を取得しながら、マップの現在地がどこなのかを感覚的に理解できるようになります。場所カードにオフセット距離を設定し、選択した場所を指すようにすることもできます。デベロッパ向けのガイダンスは、[`offset(_:)`](/documentation/SwiftUI/View/offset\(_:\))、[`accessoryOffset`](/documentation/MapKit/MKAnnotationView/accessoryOffset)および[`selectionAccessoryOffset`](/documentation/MapKitJS/Annotation/selectionAccessoryOffset)を参照してください。

### [マップ外への場所カードの追加](/jp/design/human-interface-guidelines/maps#Adding-place-cards-outside-of-a-map)

アプリやWebサイトで、場所情報をマップの外に表示することもできます。例えば、検索結果や店舗検索ツールなどのマップ以外の場所に場所のリストを表示し、ユーザが場所を選択したときに場所カードを表示したいこともあるでしょう。デベロッパ向けのガイダンスは、[`mapItemDetailSelectionAccessory(_:)`](/documentation/MapKit/MapContent/mapItemDetailSelectionAccessory\(_:\))、[`mapItemDetail(_:)`](/documentation/MapKit/MKSelectionAccessory/mapItemDetail\(_:\))および[`PlaceDetail`](/documentation/MapKitJS/PlaceDetail)を参照してください。

重要

地図表示に直接場所カードを表示しない場合は、場所カードにマップを含める必要があります。デベロッパ向けのガイダンスは、[`mapItemDetailSheet(item:displaysMap:)`](/documentation/SwiftUI/View/mapItemDetailSheet\(item:displaysMap:\))および[`init(mapItem:displaysMap:)`](/documentation/MapKit/MKMapItemDetailViewController/init\(mapItem:displaysMap:\))を参照してください。

**場所カードを開けることを知らせるために、周囲のコンテンツで場所に関連した手がかりを提供する。** 例えば、ユーザが操作して場所情報を取得できることを示すため、詳細情報を表示するボタンと合わせて、場所の名前や住所を表示します。場所を取らないデザインにするため、場所名付きのマップのピンアイコンで、場所カードが開けることを知らせることができます。

## [屋内マップ](/jp/design/human-interface-guidelines/maps#Indoor-maps)

ショッピングモールや競技場など、特定の施設に関係するアプリでは、カスタムのインタラクティブなマップをデザインして、ユーザが屋内にある見どころを見つけて移動できるようにすることができます。屋内マップには、部屋や売店などの特定のエリアを強調するオーバーレイを含めることができます。ほかにも、テキストラベル、アイコン、経路を含めることもできます。

![iPhoneに表示されているマップのスクリーンショット。サンノゼ国際空港と周辺エリアが表示されています。画面の下半分にあるカードに情報とオプションが表示されています。空港の名称、共有ボタン、カードを閉じるボタン、空港までの経路を表示するボタン、空港の電話番号に発信するボタン、空港のWebサイトを開くボタンなどがあります。](https://docs-assets.developer.apple.com/published/c2ccc1452ca8f841574b14733d971384/indoor-maps-example1%402x.png)

![iPhoneに表示されているマップのスクリーンショット。サンノゼ国際空港のターミナルBが表示されています。マップ上のターミナルの上にゲート番号が表示されています。空港の情報とオプションを含む最小化されたカードが、画面の一番下に見えています。](https://docs-assets.developer.apple.com/published/3ea0dc3c60bf548818a3b8426448a0ae/indoor-maps-example2%402x.png)

![iPhoneに表示されているマップのスクリーンショット。サンノゼ国際空港のターミナルが拡大されて表示されています。保安検査所、救護所、トイレ、エスカレーター、ゲート番号がマップに表示されています。検索フィールドと「SJCを見て回る」ボタンを含む最小化されたカードが、画面の一番下に見えています。](https://docs-assets.developer.apple.com/published/a471b49a7635bc179f3b301be886ba87/indoor-maps-example3%402x.png)

**拡大/縮小レベルに応じてマップの詳細を調整する。** 詳細な情報が多すぎると、マップが散らかって見える場合があります。部屋や建物などの大きなエリアはすべての拡大/縮小レベルで表示されるようにしてから、マップを拡大するにつれて詳細な要素やラベルが徐々に表示されるように追加していきます。空港マップの場合、縮小したマップではターミナルとゲートのみを表示し、拡大したときに個々の店舗やトイレを表示するようにするとよいでしょう。

![iPhoneに表示されているマップのスクリーンショット。拡大されて、サンノゼ国際空港のエレベーターの場所が表示されています。そのエレベーターの情報を含む最小化されたカードが、画面の一番下に見えています。](https://docs-assets.developer.apple.com/published/33153dd3e532cd4aa964be2c6e8ef58c/indoor-maps-elevator%402x.png)

**特徴のあるスタイルを使ってマップの要素を識別できるようにする。** アイコンと一緒にカラーを使うと、異なる種類のエリア、店舗、サービスが識別しやすくなり、ユーザが探している場所が見つかりやすくなります。

**複数階の施設では階を選択できるようにする。** 階を選択できるようにすると、ユーザは別の階に素早く移動できます。この機能を実装する場合は、階数を簡潔に表示してシンプルにします。ほとんどの場合、各階の名称を表示するよりも、階数の番号をリストに表示するだけで十分です。

**周辺エリアを含めてコンテキストを伝える。** 隣接する道路や公園など、近くにある場所を含めると、ユーザがマップを使用する際に方向や場所を判断しやすくなります。このようなエリアがインタラクティブな要素ではない場合は、ほかとは異なる薄いカラーで表示し、補足的な情報であることを示します。

![iPhoneに表示されているマップのスクリーンショット。拡大されて、サンノゼ国際空港のターミナルにあるゲートの番号と場所が表示されています。駐車場など、ほかのエリアには詳細が表示されていません。検索フィールドと「SJCを見て回る」ボタンを含む最小化されたカードが、画面の一番下に見えています。](https://docs-assets.developer.apple.com/published/08ddbd3ee0a11577845da5d16a52cbf3/indoor-maps-surroundings%402x.png)

**施設と周辺の交通機関を結ぶナビゲーションに対応することを検討する。** 施設と、周辺のバス停、駅、駐車場、その他の交通機関を結ぶ経路情報を提供し、施設への出入りを円滑にしましょう。追加のナビゲーションオプションを利用できるように、Appleのマップアプリに素早く切り替えられるようにしてもよいでしょう。

**施設外でのスクロールを制限する。** スクロールを制限することで、マップ上で大きくスワイプしてしまっても、ユーザが迷わないようになります。可能な場合は、屋内マップの一部が常に画面上に残るようにしてください。ユーザが迷わないように、場合によっては拡大/縮小レベルに応じてスクロールできる量を調整する必要があります。

**屋内マップをデザインするときはアプリを自然に拡張させた機能のように見せる。** Appleのマップの見た目をそのまま再現しようとするのではなく、オーバーレイ、アイコン、テキストの領域を、アプリの全体的なビジュアルスタイルに合わせてください。ガイダンスは、[Indoor Mapping Data Format](https://register.apple.com/resources/imdf/)を参照してください。

![iPhoneアプリのカスタムマップのスクリーンショット。空港のコンコースが表示されています。マップの要素はアプリのUIと一致する緑色になっています。カスタムアイコンは、ゲート、保安検査場、情報ブースを表しています。](https://docs-assets.developer.apple.com/published/af8cd30f03160d7aabe841667151058a/indoor-maps-custom-map-design%402x.png)

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/maps#Platform-considerations)

 _iOS、iPadOS、macOS、tvOS、visionOSに追加の考慮事項はありません。_

### [watchOS](/jp/design/human-interface-guidelines/maps#watchOS)

Apple Watchのマップには、場所を示した静的なスナップショットが表示されます。デザイン時にマップをインターフェイスに配置し、実行時に適切な領域を表示します。表示される領域はインタラクティブではありません。マップをタップすると、Apple Watchでマップアプリが開きます。マップに最大5つの注釈を加え、見どころやその他の関連情報を強調することはできます。デベロッパ向けのガイダンスは、[`WKInterfaceMap`](/documentation/WatchKit/WKInterfaceMap)を参照してください。

![Apple Watchに表示されているマップのスクリーンショット。Apple Parkと周辺エリアの一部が表示されています。](https://docs-assets.developer.apple.com/published/4fb62a02f6f33541fb5ba2aabe086472/maps-watch1%402x.png)

**マップインターフェイス要素を画面に合わせる。** Apple Watchの画面には、スクロールしなくても必要な要素全体が表示される必要があります。

**見どころが含まれる最小領域を表示する。** マップインターフェイス要素内のコンテンツはスクロールできないため、表示領域内に重要なコンテンツがすべて表示される必要があります。

デベロッパ向けのガイダンスは、[`WKInterfaceMap`](/documentation/WatchKit/WKInterfaceMap)を参照してください。

## [リソース](/jp/design/human-interface-guidelines/maps#Resources)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/maps#Developer-documentation)

[MapKit](/documentation/MapKit)

[MapKit JS](/documentation/MapKitJS)

[Indoor Mapping Data Format](https://register.apple.com/resources/imdf/)

#### [ビデオ](/jp/design/human-interface-guidelines/maps#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/204)

[](https://developer.apple.com/videos/play/wwdc2024/10097)

## [変更履歴](/jp/design/human-interface-guidelines/maps#Change-log)

日付| 変更内容  
---|---  
2024年12月18日| 場所カードのガイダンスとアートワークを追加。  
2023年9月12日| アートワークを追加。  
2022年9月23日| カスタム情報の表示に関するガイドラインを追加し、ベストプラクティスを改訂して、ガイダンスを1つのページに統合しました。
