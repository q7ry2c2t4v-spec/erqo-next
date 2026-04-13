# 分割ビュー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/split-views

# 分割ビュー

分割ビューは、複数の隣接するコンテンツパネルの表示を管理します。各パネルには、表、コレクション、画像、カスタムビューなどのさまざまなコンポーネントを含めることができます。

![サイドバー、キャンバス、インスペクタの3つの領域で構成されている、図案化されたウインドウ。画像は全体が、6色のオリジナルAppleロゴを連想させる赤色になっています。](https://docs-assets.developer.apple.com/published/e21fd34aed558b7161248193e22eaa76/components-split-view-intro%402x.png)

一般に分割ビューは、アプリの複数の階層レベルを一度に表示してレベル間のナビゲーションに対応する目的で使用します。このシナリオでは、ビューのプライマリパネルで項目を選択すると、その項目のコンテンツがセカンダリパネルに表示されます。セカンダリパネルの項目にさらにコンテンツが含まれる場合は、分割ビューに3次パネルを表示することもできます。

ナビゲーション用の[サイドバー](/jp/design/human-interface-guidelines/sidebars)を表示する場合は、分割ビューを使用するのが一般的です。先頭側のパネルにはアプリのトップレベルの項目やコレクションを表示し、セカンダリパネルとオプションの3次パネルには子コレクションや項目の詳細を表示できます。めったにありませんが、分割ビューを使用してプライマリビューを補完する機能グループを提供することもできます。例えばmacOSのKeynoteでは、分割ビューパネルを使用して、メインスライドキャンバスを囲む領域にスライドナビゲータ、発表者ノート、インスペクタパネルを表示しています。

## [ベストプラクティス](/jp/design/human-interface-guidelines/split-views#Best-practices)

**ナビゲーションの操作感を高めるため、詳細ビューに到達するまでの各パネルでの選択箇所を常に強調表示する。** 選択してきた経路が分かると、パネルのコンテンツ間の関係が明確になり、ユーザがナビゲーションの感覚を維持しやすくなります。

**パネル間でコンテンツのドラッグ＆ドロップに対応する。** 分割ビューでは複数の階層レベルにアクセスできるので、別のパネルへの項目のドラッグ操作に対応すれば、ユーザは、アプリ内のある箇所から別の箇所にコンテンツを簡単に移動できるようになります。ガイダンスは、[ドラッグ&ドロップ](/jp/design/human-interface-guidelines/drag-and-drop)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/split-views#Platform-considerations)

### [iOS](/jp/design/human-interface-guidelines/split-views#iOS)

**分割ビューは表示領域がコンパクトの環境ではなくレギュラーの環境で使用することを心がける。** 分割ビューでは横方向に複数のパネルが表示されるため、そのためのスペースが必要です。縦向きのiPhoneのような表示領域がコンパクトの環境では、コンテンツを折り返したり切り取ったりせずに複数のパネルを表示するのは難しいため、読みにくくなったり、操作しにくくなったりします。

### [iPadOS](/jp/design/human-interface-guidelines/split-views#iPadOS)

iPadOSの分割ビューには、垂直のパネルをメールのように2つ含めることも、Keynoteのように3つ含めることもできます。

**狭いウインドウ幅、コンパクトなウインドウ幅、中程度のウインドウ幅を考慮する。** iPadではウインドウのサイズを滑らかに変更できるため、分割ビューレイアウトのデザインを複数の幅で考慮することが重要です。特に、さまざまなパネル間を無理なく移動できるようにしてください。ガイダンスは、[レイアウト](/jp/design/human-interface-guidelines/layout)を参照してください。デベロッパ向けのガイダンスは、[`NavigationSplitView`](/documentation/SwiftUI/NavigationSplitView)および[`UISplitViewController`](/documentation/UIKit/UISplitViewController)を参照してください。

### [macOS](/jp/design/human-interface-guidelines/split-views#macOS)

macOSでは、分割ビューのパネルを水平、垂直、またはその両方に配列できます。分割ビューに表示されるパネル間の区切り線をドラッグすると、パネルのサイズを変更できます。デベロッパ向けのガイダンスは、[`HSplitView`](/documentation/SwiftUI/HSplitView)および[`VSplitView`](/documentation/SwiftUI/VSplitView)を参照してください。

![ラップトップの画面の図。左端から画面の幅の約20%の位置に垂直線があります。](https://docs-assets.developer.apple.com/published/713be8f9e61a9578b26087ad71ca6b23/vertical-split-view%402x.png)

![ラップトップの画面の図。下から画面の高さの約3分の1の位置に水平線があります。](https://docs-assets.developer.apple.com/published/8c23f101a012db47a8e2350e50432617/horizontal-split-view%402x.png)

![ラップトップの画面の図。左端近くに垂直線があり、下端近くに水平線があります。水平線は垂直線から右端に伸びています。](https://docs-assets.developer.apple.com/published/3e315fbb8f8ade8b2d3d4f105f8c4482/multiple-split-view%402x.png)

**最小と最大のパネルサイズに妥当なデフォルト値を設定する。** アプリの分割ビューでパネルのサイズを変更できるようにする場合でも、区切り線が見える範囲にとどめます。パネルが小さくなりすぎると、区切り線が消えたように見えて操作しにくくなります。

**適切な場合はユーザがパネルを非表示にできるようにする。** 例えばアプリに編集領域が含まれる場合は、ユーザがほかのパネルを非表示にして作業に集中したり、編集領域を広げたりできるようにします。Keynoteでは、ユーザがナビゲータおよび発表者ノートのパネルを非表示にして、スライドのコンテンツを編集できます。

**複数の方法で非表示のパネルを表示できるようにする。** 例えば、ツールバーのボタンやメニューコマンド（キーボードショートカットを含む）を使用して、非表示のパネルを表示できるようにします。

**細い区切り線スタイルを優先する。** 太さが1ポイントの細い区切り線を使用すれば、操作しやすさを保ちながら、コンテンツ用に最大限のスペースを確保できます。具体的なニーズがない限り、太い区切り線スタイルは使用しないでください。例えば、区切り線の両側に太線の要素を使用する表の行があるため、細い区切り線が目立たなくなる可能性がある場合は、太い区切り線の方がよいと考えられます。デベロッパ向けのガイダンスは、[`NSSplitView.DividerStyle`](/documentation/AppKit/NSSplitView/DividerStyle-swift.enum)を参照してください。

### [tvOS](/jp/design/human-interface-guidelines/split-views#tvOS)

tvOSで分割ビューを使うと、コンテンツフィルタを効果的に実装できます。プライマリパネルでユーザがフィルタのカテゴリを選択し、セカンダリパネルにその結果が表示されるという方法です。

**パネルがバランスよく配置される分割ビューレイアウトを選択する。** デフォルトでは、分割ビューのプライマリパネルに画面の幅の3分の1が、セカンダリパネルに3分の2が割り当てられますが、半分ずつのレイアウトを指定することもできます。

**分割ビューの上に1つのタイトルを表示し、ユーザがコンテンツ全体を把握できるようにする。** ユーザは分割ビューのナビゲーション操作とコンテンツのフィルタ方法をすでに知っているので、パネルごとのタイトルは必要ありません。

**タイトルの配置は、セカンダリパネルに含まれるコンテンツのタイプに応じて選択する。** 具体的には、セカンダリパネルにコンテンツのコレクションが含まれる場合には、ウインドウのタイトルを中央揃えにします。一方、セカンダリパネルに重要なコンテンツのメインビューが1つ含まれる場合は、タイトルをプライマリビューの上に配置して、コンテンツのスペースを広げることを検討します。

### [visionOS](/jp/design/human-interface-guidelines/split-views#visionOS)

**補足情報の表示には新規ウインドウではなく分割ビューを使用する。** 分割ビューは、現在のコンテキストを離れずにさらに詳しい情報にアクセスする場合に便利ですが、新規ウインドウを使用すると、コンテンツ間を移動しようとしたりコンテンツの位置を調整しようとしているユーザが戸惑う場合があります。より多くのウインドウを開くと、アプリやゲーム内のビュー同士の関係を慎重に管理する必要も生じます。ごくわずかな情報をリクエストする場合や、簡単なタスクを提示してユーザがそれを完了するまではメインタスクに戻れないようにしたい場合には、[シート](/jp/design/human-interface-guidelines/sheets)を使用してください。

### [watchOS](/jp/design/human-interface-guidelines/split-views#watchOS)

watchOSの分割ビューでは、リストビューか詳細ビューのどちらかがフルスクリーンビューとして表示されます。

**最も関連性が高い詳細ビューを自動表示する。** アプリの起動時に、最も重要な情報を表示します。例えば、ユーザの場所、時間、最近のアクションに関連する情報を表示します。

**複数の詳細ページを表示するアプリでは、詳細ビューを縦方向の[タブビュー](/jp/design/human-interface-guidelines/tab-views)に配置する。**そうすると、Digital Crownを使用して詳細ビューのタブをスクロールできるようになります。また、Digital Crownの横にページインジケータが表示されるので、タブの数と現在選択されているタブが分かります。

![Apple Watchのスクリーンショット。縦方向のタブがある詳細ビューが示されています。Digital Crownの横にあるページインジケータは、現在5つ目のタブが選択されていることを示しています。](https://docs-assets.developer.apple.com/published/8878ce079959d77e2e0e79ddb35cf470/split-view-watch-vertical-tab%402x.png)

## [リソース](/jp/design/human-interface-guidelines/split-views#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/split-views#Related)

[サイドバー](/jp/design/human-interface-guidelines/sidebars)

[タブバー](/jp/design/human-interface-guidelines/tab-bars)

[レイアウト](/jp/design/human-interface-guidelines/layout)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/split-views#Developer-documentation)

[`NavigationSplitView`](/documentation/SwiftUI/NavigationSplitView) — SwiftUI

[`UISplitViewController`](/documentation/UIKit/UISplitViewController) — UIKit

[`NSSplitViewController`](/documentation/AppKit/NSSplitViewController) — AppKit

#### [ビデオ](/jp/design/human-interface-guidelines/split-views#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/282)

## [変更履歴](/jp/design/human-interface-guidelines/split-views#Change-log)

日付| 変更内容  
---|---  
2025年6月09日| iOSとiPadOSのプラットフォームの考慮事項を追加。  
2023年12月05日| visionOSでの分割ビューに関するガイダンスを追加。  
2023年6月05日| watchOSでの分割ビューに関するガイダンスを追加。
