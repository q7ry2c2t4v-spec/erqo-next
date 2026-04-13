# ツールバー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/toolbars

2025年12月16日

Liquid Glassに関するガイダンスを更新。 

# ツールバー

ツールバーは、よく使われるコマンド、コントロール、ナビゲーション、検索にアクセスできる便利なコンポーネントです。

![図案化されたツールバー。先頭部分に「戻る」コントロールがあり、末尾部分に「その他」メニューがあります。画像全体が、6色の初代Appleロゴの赤色を連想させる赤みを帯びています。](https://docs-assets.developer.apple.com/published/3722ac9bab54e475c1fc55f2c8ddd238/components-toolbar-intro%402x.png)

ツールバーは、ビューの上端または下端に沿って横方向に配置され、論理的なセクションにグループ分けされた、1つまたは複数のコントロールセットで構成されます。

ツールバーは、ビュー内のコンテンツに作用し、ナビゲーションを円滑化し、アプリ内でユーザが自分の位置を確認するのに役立ちます。ツールバーには次の3種類のコンテンツが含まれます。

  * 現在のビューのタイトル

  * 「戻る」や「進む」のようなナビゲーションコントロールと[検索フィールド](/jp/design/human-interface-guidelines/search-fields)

  * [ボタン](/jp/design/human-interface-guidelines/buttons)や[メニュー](/jp/design/human-interface-guidelines/menus)のようなアクションまたはバー項目

ツールバーとは異なり、[タブバー](/jp/design/human-interface-guidelines/tab-bars)はアプリの領域間のナビゲーション専用です。

## [ベストプラクティス](/jp/design/human-interface-guidelines/toolbars#Best-practices)

**項目を慎重に選んで詰め込み過ぎを防ぐ。** ツールバーに項目を詰め込みすぎると、ツールバーから目的の項目を見つけて選択する操作がしづらくなります。可変の表示幅に対応するため、ツールバーが狭くなるにつれてどの項目をオーバーフローメニューに移動するかを定義します。

注意

macOSやiPadOSでは、項目が入りきらなくなると、自動的にオーバーフローメニューが追加されます。オーバーフローメニューを手動で追加しないでください。また、ツールバーの項目がデフォルトでオーバーフローするようなレイアウトは避けてください。

**追加のアクションを含めるには、「その他」メニューを追加する。** 「その他」メニューにはなるべく重要性の低いアクションを含めるようにします。可能であれば、すべてのアクションをツールバーに表示し、このメニューは本当に必要な場合にのみ追加してください。

![Macのメモアプリのスクリーンショット。利用可能なすべてのツールバー項目をツールバーに表示するのに十分なウインドウ幅があります。「その他」メニューボタンがツールバーの末尾側に表示され、その下にメニューが開いています。](https://docs-assets.developer.apple.com/published/b104e667f88497ef2ffbee94df24d8d3/toolbars-notes-app-expanded-icons%402x.png)macOSのメモの標準のツールバーには、追加のコマンドを含む「その他」メニューが表示されます。

![Macのメモアプリのスクリーンショット。ウインドウ幅が狭いため、「その他」メニューボタンを含むツールーバーの複数の項目がオーバーフローメニューに移動しています。オーバーフローメニューを開くと、その中に含まれている項目が表示されます。](https://docs-assets.developer.apple.com/published/683a0ab9a7d6cfb33cca87bcee9dffbe/toolbars-notes-app-collapsed-icons%402x.png)ウインドウの幅が狭くなると、「その他」メニューは入りきらなくなったその他のツールバー項目と共にオーバーフローメニューに移動します。

**iPadOSおよびmacOSのアプリでは、ユーザがよく使用する項目をツールバーに含めるカスタマイズを許可することを検討する。** ツールバーのカスタマイズは、多数の項目を提供するアプリ、一部のユーザのみが使用する高度な機能を含むアプリ、およびユーザが長期間使用する傾向があるアプリで特に有用です。例えば、ユーザが使用する編集コマンドの種類は各自の作業スタイルやプロジェクトによって異なることが多いため、一定範囲の編集アクションをツールバーのカスタマイズで利用可能にすると効果的です。

**ツールバーの背景や色付きのコントロールの使用を減らす。** カスタムの背景や外見を使用すると、システムで提供されている背景の効果と重なり合ったり干渉したりする可能性があります。代わりに、コンテンツレイヤーを使用してツールバーの色と外見の情報を提供し、必要な場合は[`ScrollEdgeEffectStyle`](/documentation/SwiftUI/ScrollEdgeEffectStyle)を使用してツールバー領域とコンテンツ領域を区別します。この方法は、コンテンツから注意を逸らさせずにアプリ固有の個性を表現するのに役立ちます。

**ツールバー項目のラベルとコンテンツレイヤーの背景に似たカラーを適用しない。** アプリのコンテンツレイヤーにすでに明るくカラフルなコンテンツがある場合、ツールバーにはできるだけデフォルトのモノクロの見た目を使用してください。Liquid Glassのコントロールのラベルと、コントロールの背後のコンテンツに似た色を使用すると、色の区別がつきにくくなる可能性があります。詳しいガイダンスは[Liquid Glassカラー](/jp/design/human-interface-guidelines/color#Liquid-Glass-color)を参照してください。

**ツールバーにはなるべく標準コンポーネントを使用する。** デフォルトでは、標準のボタン、テキストフィールド、ヘッダ、フッタには、バーのコーナーと同心になるようなコーナー半径が使用されます。カスタムコンポーネントを作成する必要がある場合は、そのコンポーネントのコーナー半径もバーのコーナーと同心になるようにしてください。

**ツールバー内でセグメントコントロールを使用しない。** ツールバーは現在のビューに対するアクションを実行するコンポーネントで、セグメントコントロールはコンテキストを切り替えるときに使うコンポーネントです。ガイダンスは[セグメントコントロール](/jp/design/human-interface-guidelines/segmented-controls)を参照してください。

**操作に集中できるように、ツールバーを一時的に非表示にすることを検討する。** 最小限のインターフェイスは、余計な要素を減らしたり、コンテンツの表示領域を増やしたりするのに役立ちます。この機能に対応する場合は、最も有用な場面で文脈に沿って実行し、非表示のインターフェイス要素を確実に復元する手段を提供してください。ガイダンスは、[フルスクリーンモード](/jp/design/human-interface-guidelines/going-full-screen)を参照してください。visionOSに特有のガイダンスは、[イマーシブ体験](/jp/design/human-interface-guidelines/immersive-experiences)を参照してください。

## [タイトル](/jp/design/human-interface-guidelines/toolbars#Titles)

**ウインドウごとに分かりやすいタイトルを付ける。** タイトルは、ユーザがアプリ内を移動する際に現在位置を確認し、開いている複数のウインドウのコンテンツを見分ける手段になります。ツールバーのタイトルが冗長に感じられる場合は、タイトル領域を空のままにできます。例えば「メモ」でウインドウが1つだけ開いている場合は、一般にコンテンツの1行目で十分にコンテキストを提供できるため、現在のメモにタイトルは表示されません。一方、別々のウインドウでメモを開いている場合は、ユーザが見分けられるようにコンテンツの1行目を使ったタイトルが表示されます。

**アプリ名をウインドウのタイトルにしない。** アプリ名はコンテンツ階層やアプリ内のウインドウまたは領域についての有用な情報ではないので、タイトルとして適切ではありません。

**タイトルは簡潔にする。** ウインドウやビューの目的を1語または短いフレーズにまとめることを目指します。ほかのコントロール用に十分なスペースを確保するため、タイトルの長さは15文字以内に抑えてください。

## [ナビゲーション](/jp/design/human-interface-guidelines/toolbars#Navigation)

ナビゲーションコントロールを含むツールバーは、ウインドウの上部に表示され、コンテンツの階層内の移動を補助するコンポーネントです。ツールバーには多くの場合、コンテンツの領域や一部分の間を素早く移動するための[検索フィールド](/jp/design/human-interface-guidelines/search-fields)も含まれています。iOSでは、ナビゲーション専用のツールバーをナビゲーションバーと呼ぶことがあります。

**標準の「戻る」ボタンと「閉じる」ボタンを使用する。** ユーザは、標準の「戻る」ボタンを使用して情報の階層内の手順をたどり、標準の「閉じる」ボタンを使用してモーダルビューを閉じることを知っています。これらのボタンには、それぞれ標準のシンボルを優先して使用し、 _戻る_ や _閉じる_ のようなテキストラベルを使用しないでください。カスタムバージョンのボタンを作成する場合は、そのボタンが同じボタンとして認識されること、ユーザの期待通りに動作すること、インターフェイスのその他の部分と調和すること、およびアプリやゲーム全体で一貫して実装されていることを確認してください。ガイダンスは、[アイコン](/jp/design/human-interface-guidelines/icons)を参照してください。

![先頭側に配置した「戻る」シンボルと末尾側に配置した「戻る」テキストをグループ化した、カプセル型の「戻る」ボタンの図。](https://docs-assets.developer.apple.com/published/4e68808e84d4d6063c99d111b883cfb0/toolbars-navigation-action-back-incorrect%402x.png)

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![標準の「戻る」シンボルを含む、標準の円形の「戻る」ボタンの図](https://docs-assets.developer.apple.com/published/bf5f1cf48120b10f031bd9df57124f0f/toolbars-navigation-action-back-correct%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

## [アクション](/jp/design/human-interface-guidelines/toolbars#Actions)

**ユーザが実行する主なタスクに合わせてアクションを提供する。** 基本的に、ユーザが必要とする可能性が高いコマンドを優先してください。通常、それらのコマンドはユーザがよく使うコマンドです。ただし、ユーザが操作する最上位のオブジェクトや最も重要なオブジェクトに当てはまるコマンドを適宜優先してかまいません。

**各コントロールの意味を必ず明確にする。** 勘に頼ったり試しに使ってみたりしないと機能が分からないようなツールバーの項目は避けましょう。シンボルではうまく表すことができない _編集_ のようなアクションを除き、テキストよりもシンプルで認識しやすいシンボルを優先して使用してください。一般的なアクションを表すシンボルについてのガイダンスは、[標準のアイコン](/jp/design/human-interface-guidelines/icons#Standard-icons)を参照してください。

![「フィルタ」、「削除」、「新規」のテキストボタンラベルを含む項目グループの図。](https://docs-assets.developer.apple.com/published/76061301992af8f39c43cfd4eb651e47/toolbars-prefer-symbols-incorrect%402x.png)

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![「フィルタ」、「削除」、「新規」のシンボルボタンラベルを含む項目グループの図。](https://docs-assets.developer.apple.com/published/a90ab6d6f58aa023f4b830e4045b507b/toolbars-prefer-symbols-correct%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

**システムが提供するシンボルを枠線なしで表示する。** システムが提供するシンボルはユーザになじみがあり、自動的に適切な色とバイブランスが適用され、ユーザの操作に対していつでも一貫した反応をします。このセクションには目に見えるコンテナがあり、ホバー状態と選択状態の見た目が自動的に定義されているため、枠線（枠の付いた円形のシンボルなど）は不要です。ガイダンスは、[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)を参照してください。

![「フィルタ」と「その他」のボタンを含む項目グループの図。ボタンにはシンボルのラベルと円形の枠線が付いています。](https://docs-assets.developer.apple.com/published/90f36d797636e931c39663c146c1cb11/toolbars-icons-circle-outline-incorrect%402x.png)

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![「フィルタ」と「その他」のボタンを含む項目グループの図。ボタンにはシンボルのラベルが付いていますが、枠線はありません。](https://docs-assets.developer.apple.com/published/e7b2189bb13488aab5e7eacc5eea9b1b/toolbars-icons-no-outline-correct%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

**「完了」や「送信」などの主要なアクションには`.prominent`スタイルを使用する。**これにより、アクションが区別されて色合いが調整され、焦点が明確になります。プライマリアクションを1つだけ指定し、それをツールバーの末尾側に配置してください。

![先頭側の「フィルタ」ボタンと末尾側の「完了」ボタンからなる2つのツールーバー項目の図。ボタンはグループ化されておらず、「完了」ボタンにはプライマリアクションであることを示すprominentスタイルが適用されています。](https://docs-assets.developer.apple.com/published/36c552c629c8a980c83501134e53d749/toolbars-prominent-action-tinted%402x.png)

## [項目のグループ化](/jp/design/human-interface-guidelines/toolbars#Item-groupings)

ツールバーの項目は、ツールバーの先頭部分、中央部分、末尾部分の3か所に配置できます。これらの領域は、ナビゲーションコントロール、ウインドウまたは書類のタイトル、一般的なアクション、および検索の配置場所としてよく知られています。

  * **先頭部分。** 直前の書類に戻ったり、サイドバーを表示または非表示にしたりするための要素がバーの先頭部分に表示されます。その次に、ビューのタイトルが表示されます。タイトルの次には書類メニューを表示できます。このメニューには、「複製」、「名称変更」、「移動」、「書き出す」など書類全体に影響する標準およびアプリ固有のコマンドを含めます。これらの項目を常に利用できるようにするため、ツールバーの先頭部分の項目はカスタマイズできないようになっています。

  * **中央部分。** 中央部分には、よく使われている便利なコントロールが表示されます。ビューのタイトルを先頭部分に表示できない場合は、ここに表示できます。macOSとiPadOSでは、ユーザにツールバーのカスタマイズを許可した場合、中央部分の項目の追加、削除、並べ替えができます。ここに配置される項目は、ウインドウが縮小して全部が収まりきらなくなると、システムが管理するオーバーフローメニューに自動的に移されます。

  * **末尾部分。** 末尾部分には、常に利用可能にしておく必要のある重要な項目、近くのインスペクタを開くボタン、検索フィールド（任意）、および追加項目を含み、ツールバーのカスタマイズに対応する「その他」メニューが表示されます。ここには、「完了」のようなプライマリアクションも（あれば）配置されます。末尾部分の項目はどのウインドウサイズでも常に表示されます。

![iPadのフリーボードアプリの上部にあるツールバーの図。コールアウトは、ツールバーの項目をグループ化する位置（先頭部分、中央部分、末尾部分）を示します。](https://docs-assets.developer.apple.com/published/87d7186527cfde64f91bafafcec1a816/toolbars-ipad-anatomy%402x.png)

目的のグループに項目を配置するには、先頭部分、中央部分、または末尾部分に項目をピン留めし、必要に応じてボタンやその他の項目の間にスペースを挿入します。

**ツールバー項目は機能や使用頻度に応じて論理的にグループ分けする。** 例えばKeynoteでは、プレゼンテーションに関するコマンド、再生のコマンド、オブジェクトの挿入のように、機能ごとに複数のセクションがあります。

**ナビゲーションコントロールと「完了」、「閉じる」、「保存」などの重要なアクションを専用の見分けやすいセクションにグループ分けする。** これはアクションの重要性を反映しており、ユーザがこれらのアクションを見つけて理解するのに役立ちます。

![iPhoneの上部にあるツールバーの図。「戻る」、「進む」、ツール選択の各コントロールと「その他」メニューが末尾側の1つのセクションにグループ化されています。](https://docs-assets.developer.apple.com/published/9349ac4f406f84c24e98a6b9445b9560/toolbars-layout-grouping-incorrect%402x.png)

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![iPhoneの上部にあるツールバーの図。「戻る」と「進む」のコントロールが先頭側でグループ化され、ツール選択のコントロールと「その他」メニューが末尾側でグループ化されています。](https://docs-assets.developer.apple.com/published/2fede653e14b982c4b2c65f3ca657278/toolbars-layout-grouping-correct%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

**プラットフォーム間でグループ分けと配置の一貫性を保つ。** これにより、ユーザはアプリに慣れ親しんで、どこで使用しても同じ動作をするという信頼感を得ることができます。

**グループの数は最小限に抑える。** グループが多すぎると、iPadやMacでスペースに余裕がある場合でも、ツールバーが雑然として混乱を招きます。基本的に、3つ以内に抑えてください。

**テキストラベル付きのアクションは別々に配置する。** テキストラベル付きのアクションを記号付きのアクションの隣に配置すると、テキストと記号が組み合わさった1つのアクションのように見えてしまい、混乱や誤解を招きます。テキストラベルのあるボタンがツールバーに複数含まれる場合は、それらのボタンのテキストがつながって表示されて、ボタンを区別できなくなる可能性があります。ボタンの間に固定スペースを挿入して区切りを追加してください。デベロッパ向けのガイダンスは、[`UIBarButtonItem.SystemItem.fixedSpace`](/documentation/UIKit/UIBarButtonItem/SystemItem/fixedSpace)を参照してください。

![iPhoneの上部にあるツールバーの図。テキストラベル付きの「編集」コントロールと記号付きの「共有」コントロールが末尾側でグループ化されています。](https://docs-assets.developer.apple.com/published/503413fea667e01111c76f821912670a/toolbars-layout-text-action-grouping-incorrect%402x.png)

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![iPhoneの上部にあるツールバーの図。テキストラベル付きの「編集」コントロールと記号付きの「共有」コントロールが末尾側の別個のセクションにグループ化されています。](https://docs-assets.developer.apple.com/published/6d2bd80dd07268d7bd16d2b5242f7b3d/toolbars-layout-text-action-grouping-correct%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/toolbars#Platform-considerations)

 _tvOSに追加の考慮事項はありません。_

### [iOS](/jp/design/human-interface-guidelines/toolbars#iOS)

**メインツールバー領域には特に重要な項目のみを含めるようにする。** スペースが限られているため、アプリに必要不可欠なアクションを慎重に検討し、それらを先に含めてください。追加項目を含めるには、「その他」メニューを作成します。

**ユーザが移動したりスクロールしたりしても常に自分の位置が分かるように、大きなタイトルを使用する。** デフォルトでは、ユーザがコンテンツのスクロールを開始すると大きなタイトルが標準タイトルに遷移し、一番上までスクロールすると大きなタイトルに戻って、ユーザに現在の位置を再認識させます。デベロッパ向けのガイダンスは、[`prefersLargeTitles`](/documentation/UIKit/UINavigationBar/prefersLargeTitles)を参照してください。

### [iPadOS](/jp/design/human-interface-guidelines/toolbars#iPadOS)

**ツールバーとタブバーをまとめることを検討する。** iPadOSでは、ツールバーと[タブバー](/jp/design/human-interface-guidelines/tab-bars)をビューの上部にある同じ横方向のスペースに共存させることができます。これは、ウインドウの幅いっぱいにコンテンツを表示しながら、複数のメインアプリ領域の間を移動する必要があるレイアウトで特に便利です。ガイダンスは、[レイアウト](/jp/design/human-interface-guidelines/layout)と[ウインドウ](/jp/design/human-interface-guidelines/windows)を参照してください。

### [macOS](/jp/design/human-interface-guidelines/toolbars#macOS)

macOSのアプリでは、ツールバーはウインドウ上部のフレーム内に配置され、タイトルバーの下に表示されるかタイトルバーと一体化します。ウインドウタイトルはコントロールと一緒にインラインで表示でき、ツールバー項目はベゼルを含みません。

![macOSのFinderウインドウの図。ツールバーとウインドウフレームの位置を示すコールアウトが付いています。](https://docs-assets.developer.apple.com/published/8c85552a523462f900a00d0e054fe4b0/toolbars-mac-window-anatomy%402x.png)

**ツールバーのすべての項目をメニューバーのコマンドとしても利用できるようにする。** ツールバーはユーザがカスタマイズしたり非表示にしたりする可能性があるので、ここにしかコマンドが表示されないということがないようにしてください。反対に、すべてのメニュー項目をツールバーの項目として提供するのも適切とは言えません。すべてのメニューコマンドが、ツールバー内に場所を確保するほど重要性や使用頻度が高いわけではないからです。

### [visionOS](/jp/design/human-interface-guidelines/toolbars#visionOS)

visionOSの場合、システム提供のツールバーは、ウインドウの下端に沿ってウインドウ管理コントロールの上に表示され、ウインドウに平行な平面上（ウインドウより少し手前にある）に配置されます。

![visionOSのメモアプリウインドウの下端に沿って表示されているツールバーのスクリーンショット。](https://docs-assets.developer.apple.com/published/47985b0aebd160790502368ff9e282a1/visionos-toolbar-notes-app%402x.png)

ツールバー項目の背後でコンテンツがスクロールしても項目の読みやすさが損なわれないよう、visionOSではバーの背景に可変ブラーを使用します。可変ブラーによって、ビューのガラスマテリアルの統一感と一体感を維持したまま、コンテンツがスクロール中でもバーが動かないようにできます。

visionOSでは、ツールバーの各項目に記号またはテキストラベルを割り当てることができます。visionOSでは、ユーザが記号を含むツールバー項目を見つめると、テキストラベルが現れて追加情報が提供されます。

**システム提供のツールバーを使用することが望ましい。** 標準ツールバーは、ほかと一貫性があって馴染みのある見た目をしており、視線や手で使いやすいように最適化されています。また、ウインドウに対して適切な位置に自動的に配置されます。

![visionOSのツールバーのスクリーンショット。](https://docs-assets.developer.apple.com/published/449acaaf0268d1fff08e9bf41b7c82d9/visionos-toolbar-standard-layout%402x.png)

**縦型のツールバーを作成することは避ける。** visionOSでは、[タブバー](/jp/design/human-interface-guidelines/tab-bars)が縦型なので、ツールバーを縦に表示するとユーザが混乱する可能性があります。

**ウインドウのサイズがツールバーの幅より狭くならないようにする。** visionOSには、各アプリのアクションを一覧表示するメニューバーがありません。そのため、ウインドウのサイズに関係なく、ツールバーから重要なコントロールに確実にアクセスできるようにしておくことが重要です。

**アプリがモーダル状態に遷移したときに、そのコンテキストに関連するツールバーコントロールを提供することを検討する。** 例えば写真編集アプリの場合は、複数の手順からなる編集タスクを実行しやすいようにモーダル状態に遷移することがあるかもしれません。このモーダルな編集ビューには、メインウインドウのコントロールとは異なるコントロールを表示するようにします。ただし、アプリがモーダル状態を出たときには、ウインドウの標準ツールバーのコントロールを復活させるようにしてください。

**ツールバー内でプルダウンメニューを使用しない。** プルダウンメニューを含めることで、ツールバー項目に関連するアクションを追加で提供できます。ただし、ユーザにとって見つけにくかったり、インターフェイスがごちゃごちゃしたりする可能性があります。また、visionOSではツールバーがウインドウの下端にあるため、その下にある標準ウインドウコントロールがプルダウンメニューによって見えにくくなることもあるかもしれません。ガイダンスは、[プルダウンボタン](/jp/design/human-interface-guidelines/pull-down-buttons)を参照してください。

### [watchOS](/jp/design/human-interface-guidelines/toolbars#watchOS)

ツールバーボタンを使用すると、関連するコンテンツを表示するビューで重要なアプリ機能を提供できます。ツールバーのボタンは上隅または画面下部に配置できます。ツールバーのボタンをスクロールするコンテンツの上に配置すると、下にあるコンテンツがスクロールされても、ボタンは常に表示されます。

![上部の先頭および末尾の端にあるツールバーのボタンのスクリーンショット。](https://docs-assets.developer.apple.com/published/464c7be02e97dcb7470c9b8202dc2b59/toolbars-watch-top-buttons%402x.png)

上部のツールバーのボタン

![下部の先頭および末尾にある2つのツールバーのボタンのスクリーンショット。](https://docs-assets.developer.apple.com/published/53d742601fa4b250207336099587e1d3/toolbars-watch-bottom-buttons%402x.png)

下部のツールバーのボタン

デベロッパ向けのガイダンスは、[`topBarLeading`](/documentation/SwiftUI/ToolbarItemPlacement/topBarLeading)、[`topBarTrailing`](/documentation/SwiftUI/ToolbarItemPlacement/topBarTrailing)、または[`bottomBar`](/documentation/SwiftUI/ToolbarItemPlacement/bottomBar)を参照してください。

ボタンをスクロールするビューに配置することもできます。デフォルトで、スクロールするツールバーボタンは、ユーザが上にスクロールして表示しない限り隠れています。ユーザはスクロールビューの上まで頻繁にスクロールするので、ツールバーボタンは自動的にユーザに認知されます。

![上部の先頭および末尾にある2つのツールバーのボタンのスクリーンショット。ツールバーのスクロールビューにはプライマリアクションボタンも含まれていますが、表示されていません。](https://docs-assets.developer.apple.com/published/027a24ac805a9e7976a1ccd1df68f0d3/toolbars-watch-primary-button-hidden%402x.png)

ツールバーのボタンは表示されていません

![上部の先頭および末尾にある2つのツールバーのボタンのスクリーンショット。ツールバーのスクロールビューには、プライマリアクションボタンも表示されています。](https://docs-assets.developer.apple.com/published/e010a0cdf42f792ebb4715cdd5f65676/toolbars-watch-primary-button-visible%402x.png)

ツールバーのボタンが表示されています

デベロッパ向けのガイダンスは、[`primaryAction`](/documentation/SwiftUI/ToolbarItemPlacement/primaryAction)を参照してください。

**スクロールするツールバーボタンは、アプリの主要機能ではないが重要なアクションに使用する。** ツールバーボタンには、アプリの重要な機能をそれと関連するビュー（ただし必ずしもその機能のためのビューではない）で提供できるという柔軟性があります。例えば「メール」では、「受信」ビューの上にあるツールバーボタンから、非常に重要な「新規メッセージ」アクションを実行できます。「受信」の主な目的はメールメッセージのスクロールリストを表示することであるため、このビューの最上部のツールバーボタンで、ビューとの関わりが深いメール作成アクションを実行できるようにすることは理にかなっています。

## [リソース](/jp/design/human-interface-guidelines/toolbars#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/toolbars#Related)

[サイドバー](/jp/design/human-interface-guidelines/sidebars)

[タブバー](/jp/design/human-interface-guidelines/tab-bars)

[レイアウト](/jp/design/human-interface-guidelines/layout)

[ボタン](/jp/design/human-interface-guidelines/buttons)

[検索フィールド](/jp/design/human-interface-guidelines/search-fields)

[Appleデザインリソース](https://developer.apple.com/design/resources/)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/toolbars#Developer-documentation)

[ツールバー](/documentation/SwiftUI/Toolbars) — SwiftUI

[`UIToolbar`](/documentation/UIKit/UIToolbar) — UIKit

[`NSToolbar`](/documentation/AppKit/NSToolbar) — AppKit

#### [ビデオ](/jp/design/human-interface-guidelines/toolbars#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/356)

## [変更履歴](/jp/design/human-interface-guidelines/toolbars#Change-log)

日付| 変更内容  
---|---  
2025年12月16日| Liquid Glassに関するガイダンスを更新。  
2025年6月09日| バー項目のグループ化に関するガイダンスを追加し、シンボルの使い方に関するガイダンスを更新し、ナビゲーションバーのガイダンスを追加。  
2023年6月21日| visionOSのガイダンスを追加するために更新。  
2023年6月05日| watchOSでのツールバーの使い方に関するガイダンスを更新。
