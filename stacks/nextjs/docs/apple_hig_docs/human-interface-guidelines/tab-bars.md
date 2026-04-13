# タブバー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/tab-bars

2025年12月16日

Liquid Glassに関するガイダンスを更新。 

# タブバー

タブバーを使うと、アプリのトップレベルのセクション間を移動できます。

![名前のある4つのプレースホルダアイコンを含む、図案化されたタブバー。画像全体が、6色の初代Appleロゴの赤色を連想させる赤みを帯びています。](https://docs-assets.developer.apple.com/published/2856c6f5459627a283019c5d49942992/components-tab-bar-intro%402x.png)

タブバーは、アプリで提供する異なるタイプの情報や機能をユーザに理解してもらうのに役立ちます。また、セクション内の現在のナビゲーション状態を維持したまま、ビューのセクションを素早く切り替えることもできます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/tab-bars#Best-practices)

**タブバーは、アクションの実行ではなくナビゲーションのために使用する。** タブバーは、時計アプリの「アラーム」タブ、「ストップウォッチ」タブ、「タイマー」タブのように、アプリの異なるセクション間を移動できるようにするためのものです。現在のビュー内の要素に対して実行するコントロールを提供する場合は、代わりに[ツールバー](/jp/design/human-interface-guidelines/toolbars)を使用してください。

**アプリの別のセクションに移動してもタブバーが表示されたままになるようにする。** タブバーを非表示にすると、アプリのどの場所にいるか分からなくなる場合があります。例外は、モーダルビューがタブバーを覆う場合です。モーダルは一時的で自己完結型であるためです。

**アプリのナビゲーションに必要なタブは適切な数にする。** アプリの階層を表現するものとして、タブが増えることによる複雑さと、ユーザが頻繁に各セクションにアクセスする必要性とのバランスを検討することが重要です。通常は、タブが少ない方がナビゲーションしやすい点を考慮してください。可能な場合は、複雑な情報構造を持つアプリでの代替案として、サイドバーやサイドバーに変換可能なタブバーを検討してください。

**タブがはみ出ないようにする。** デバイスのサイズや向きによっては、すべてのタブが見えない場合があります。横方向のスペースの関係で見えるタブの数が限られている場合、iOSとiPadOSでは末尾のタブが「その他」タブになり、残りの項目が別のリストに表示されます。「その他」タブができると、非表示になったタブのコンテンツを開いたり気付いたりしにくくなるので、これが起こらないようにしてください。

**コンテンツが利用できなくても、タブバーのボタンは無効または非表示にしない。** タブバーのボタンが利用できたりできなかったりすると、アプリのインターフェイスが不安定で予測できないものになります。セクションが空の場合は、なぜコンテンツが利用できないかを説明します。

**ナビゲーションに役立つようにタブにラベルを追加する。** タブのラベルはタブバーのアイコンの下または横に表示されます。タブに含まれるコンテンツや機能のタイプを明確に説明する分かりやすいタブラベルにすると、ナビゲーションがやりやすくなります。可能な場合は常に、短い言葉を使います。

**使い慣れたスケーラブルなタブバーのアイコンにするためにSF Symbolsの使用を検討する。**[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)を使用すると、各コンテキストに応じてタブバーのアイコンの見た目が自動的に変化します。例えば、デバイスと向きに応じてレギュラーまたはコンパクトのタブバーになります。コンパクトビューではタブバーのアイコンがタブのラベルの上に表示されますが、レギュラービューではアイコンとラベルが横に並べて表示されます。プラットフォームとの一貫性を保つため、シンボルやアイコンは塗りつぶしのものを使うことをおすすめします。

![2台のiPhoneデバイスが並んだ図。最初のiPhoneは横向きで、画面下部にタブバーがあり、各タブの先頭側にはタブバーアイコン、末尾側にはタブラベルが表示されています。2台目のiPhoneは縦向きで、画面下部にタブバーがあり、タブバーアイコンがそれぞれのタブラベルの上に表示されています。](https://docs-assets.developer.apple.com/published/c4fafe5d25bf267f3d4411165c393c96/tab-bar-landscape%402x.png)

カスタムのタブバーアイコンを作成する場合は、[Appleのデザインリソース](https://developer.apple.com/design/resources/)でタブバーのアイコンのサイズを確認してください。

![タブバーの図。タブバーのアイコンとタブのラベルの位置を示すコールアウトが付いています。](https://docs-assets.developer.apple.com/published/230bf3c10d2cb71da1bd5df7ac1981d3/tab-bar-anatomy-callouts%402x.png)

**バッジを使用して重要な情報があることを伝える。** タブにバッジ（白いテキストの数字か感嘆符を含む赤い楕円形）を表示すると、セクションに新しい情報やアップデートされた情報があることを示すことができます。これにより、ユーザの注意を引くことができます。バッジは重要な情報でのみ使用するようにして、そのインパクトと意味が薄れることがないようにします。ガイダンスは、[通知](/jp/design/human-interface-guidelines/notifications)を参照してください。

![縦向きになったiPhoneの下半分の図。画面の一番下にタブバーが配置されています。2つのタブに赤丸のバッジが付いており、重要な情報があることを示しています。](https://docs-assets.developer.apple.com/published/29a93bc69eaa415e2e3d5440474a8d36/tab-bar-badges-iphone%402x.png)

**タブのラベルとコンテンツレイヤーの背景に似たカラーを適用しない。** アプリのコンテンツレイヤーにすでに明るくカラフルなコンテンツがある場合、タブバーにはできるだけモノクロの見た目を使用するか、視覚的に十分に異なるアクセントカラーを選択してください。詳しいガイダンスは[Liquid Glassカラー](/jp/design/human-interface-guidelines/color#Liquid-Glass-color)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/tab-bars#Platform-considerations)

 _macOSに追加の考慮事項はありません。watchOSには対応していません。_

### [iOS](/jp/design/human-interface-guidelines/tab-bars#iOS)

タブバーは、画面下のコンテンツの上に表示されます。項目は[Liquid Glass](/jp/design/human-interface-guidelines/materials#Liquid-Glass)の背景の上に表示され、下にあるコンテンツが透けて見えます。

「ミュージック」のミニプレーヤーのようなアクセサリが付いたタブバーでは、ユーザが下にスクロールしたときにタブバーを最小化し、アクセサリをタブバーに含めて移動することができます。タブをタップするか、ビューの一番上までスクロールすると、最小化した状態を解除できます。デベロッパ向けのガイダンスは、[`TabBarMinimizeBehavior`](/documentation/SwiftUI/TabBarMinimizeBehavior)および[`UITabBarController.MinimizeBehavior`](/documentation/UIKit/UITabBarController/MinimizeBehavior)を参照してください。

![縦向きになったiPhoneの下半分の図。ミュージックアプリが開いています。画面下部のタブバーの上にミニプレーヤーが開いています。](https://docs-assets.developer.apple.com/published/665567ae809c1da7ed742a2482217721/tab-bar-with-accessory-expanded%402x.png)

アクセサリつきの展開されたタブバー

![縦向きになったiPhoneの下半分の図。ミュージックアプリが開いています。タブバーが最小化され、現在開いているタブとして画面下の先頭側に表示されています。下の中央にはミニプレーヤーが、末尾側には,検索タブがあります。](https://docs-assets.developer.apple.com/published/2890dde46c7bb36175d2f1dfd360d35c/tab-bar-with-accessory-collapsed%402x.png)

アクセサリつきの最小化されたタブバー

タブバーの末尾側には、明確に区別された検索項目を含めることができます。ガイダンスは[検索フィールド](/jp/design/human-interface-guidelines/search-fields)を参照してください。

### [iPadOS](/jp/design/human-interface-guidelines/tab-bars#iPadOS)

タブバーは画面上部近くに表示されます。タブバーを固定要素として表示することも、タブバーをサイドバーに切り替えるボタンを含めることも選択できます。デベロッパ向けのガイダンスは、[`tabBarOnly`](/documentation/SwiftUI/TabViewStyle/tabBarOnly)および[`sidebarAdaptable`](/documentation/SwiftUI/TabViewStyle/sidebarAdaptable)を参照してください。

![iPadのミュージックアプリのスクリーンショット。画面上部近くにタブバーがあります。](https://docs-assets.developer.apple.com/published/1715e818d2c2e32dc25c96e3b5923146/ipad-tab-bar-music-app%402x.png)

![iPadのミュージックアプリのスクリーンショット。画面の先頭側にサイドバーに変換されたタブバーがあります。](https://docs-assets.developer.apple.com/published/a939701b0ea36271f24ecfc709bbf939/ipad-sidebar-music-app%402x.png)

備考

タブバーへの切り替えオプションなしでサイドバーを表示するときは、タブビューではなく[ナビゲーションの分割ビュー](https://developer.apple.com/documentation/swiftui/navigationsplitview)を使用してください。ガイダンスは、[サイドバー](/jp/design/human-interface-guidelines/sidebars)を参照してください。

**ナビゲーションにはタブバーを優先して使う。** タブバーを使用すると、ユーザが最もよく使用するアプリのセクションにアクセスできます。アプリが複雑である場合は、タブバーをサイドバーに変換できるようにすると、幅広いナビゲーションオプションを提供できます。

**ユーザがタブバーをカスタマイズできるようにする。** ユーザがアクセスする可能性があるセクションが多いアプリでは、ユーザがよく使う項目を選択してタブバーに追加したり、使用頻度の低い項目を削除したりできるようにすると便利です。例えば、ミュージックアプリでは、タブバーに表示するお気に入りのプレイリストを選択できます。ユーザが自分でタブを選べるようにする場合は、コンパクトビューとレギュラービューでサイズの一貫性を保つため、デフォルトのリストを5つ以内に収めることを目指してください。デベロッパ向けのガイダンスは、[`TabViewCustomization`](/documentation/SwiftUI/TabViewCustomization)および[`UITab.Placement`](/documentation/UIKit/UITab/Placement)を参照してください。

### [tvOS](/jp/design/human-interface-guidelines/tab-bars#tvOS)

タブバーはカスタマイズ性が高く、例えば以下のようなことができます:

  * タブバーの背景のティント、カラー、画像を指定する

  * タブの項目のフォントを選択する（選択中の項目のフォントを変えるなど）

  * 選択中の項目と選択していない項目のティントを指定する

  * 設定や検索などのボタンアイコンを追加する

タブバーはデフォルトでは透明です。選択中のタブのみ不透明になります。リモコンでタブバーにフォーカスすると、選択したタブにドロップシャドウが付き、選択状態が強調されます。タブバーの高さは68ポイントで、上端は画面上部から46ポイントです。この値はどちらも変更できません。

項目がタブバーに収まりきらない場合、右端の項目が途中で切れ、タブバーの右側を起点にしたフェードエフェクトが適用されます。項目が多くスクロールが発生する場合は、左側の表示切れに対しても、左側を起点にしたフェードエフェクトが適用されます。

**タブバーのスクロール動作に注意する。** 現在のタブに含まれるメインビューが1つだけの場合、タブバーはデフォルトで画面外にスクロールできます。この動作の例は、TVアプリの「今すぐ観る」、「映画」、「テレビ番組」、「スポーツ」、「キッズ」タブで確認できます。ただし、TVアプリの「ライブラリ」タブやアプリの「設定」画面など、画面に分割ビューが含まれている場合はスクロールできません。この場合、分割ビューのプライマリパネルとセカンダリパネルのコンテンツをスクロールしても、タブバーはビューの上部から動きません。リモコンの「メニュー」を押すと、タブのコンテンツによらず、フォーカスが常にページ上部のタブバーに戻ります。

**ライブビューイングアプリでは、一貫性のある方法でタブを整理する。** ライブストリーミングアプリで最適な体験を実現するには、コンテンツをタブで整理する際に、次の順序に従います。

  * ライブコンテンツ

  * クラウドDVRまたはその他の録画コンテンツ

  * その他のコンテンツ

ガイダンスは、[ライブビューイングアプリ](/jp/design/human-interface-guidelines/live-viewing-apps)も参照してください。

### [visionOS](/jp/design/human-interface-guidelines/tab-bars#visionOS)

visionOSでは、タブバーは常に縦型で、ウインドウの先頭側を基準にして固定された位置に浮いています。ユーザがタブバーを見つめるとタブバーが自動的に拡大します。特定のタブを開くにはタブを見つめてからタップします。タブバーが拡大している間は、その背後にあるコンテンツが一時的に見えにくくなることがあります。

以下のカスタムコントロールを使用できます 

このビデオコンテンツの説明: visionOSアプリのウインドウの横に表示されたタブバーを大きく映した録画。タブバーには記号のみが含まれています。見つめている人がいることを示すため、現在選択されているタブには、ホバーエフェクトが適用されます。また、バーが拡大して記号とラベルの両方が表示されます。 

再生 

**各タブに記号とテキストラベルを割り当てる。** タブの記号は常にタブバーに表示され、ユーザがタブバーを見つめたときにはタブラベルも表示されます。タブバーは広がりますが、ユーザが一目で読めるようにタブラベルは短くしておく必要があります。

![閉じたタブバーを示しているスクリーンショット。記号のみが含まれています。](https://docs-assets.developer.apple.com/published/60282ea47a438f5b2bd84705212b44e4/visionos-tab-bar-collapsed%402x.png)閉じている

![広がったタブバーを示しているスクリーンショット。記号とラベルの両方が含まれています。](https://docs-assets.developer.apple.com/published/df1a14ce3d5e2743bfdfb0fea47fc340/visionos-tab-bar-expanded%402x.png)広がっている

**適宜タブ内でサイドバーを使用することを検討する。** アプリの階層が深い場合は、タブ内での2次的なナビゲーションを可能にするために[サイドバー](/jp/design/human-interface-guidelines/sidebars)を使用することをおすすめします。タブでサイドバーを使用する場合は、サイドバーでの選択によって表示中のタブが変わらないようにしてください。

## [リソース](/jp/design/human-interface-guidelines/tab-bars#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/tab-bars#Related)

[タブビュー](/jp/design/human-interface-guidelines/tab-views)

[ツールバー](/jp/design/human-interface-guidelines/toolbars)

[サイドバー](/jp/design/human-interface-guidelines/sidebars)

[マテリアル](/jp/design/human-interface-guidelines/materials)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/tab-bars#Developer-documentation)

[`TabView`](/documentation/SwiftUI/TabView) — SwiftUI

[`TabViewBottomAccessoryPlacement`](/documentation/SwiftUI/TabViewBottomAccessoryPlacement) — SwiftUI

[タブナビゲーションでアプリのコンテンツを強化する](/documentation/SwiftUI/Enhancing-your-app-content-with-tab-navigation) — SwiftUI

[`UITabBar`](/documentation/UIKit/UITabBar) — UIKit

[タブバーとサイドバーでiPadアプリを向上させる](/documentation/UIKit/elevating-your-ipad-app-with-a-tab-bar-and-sidebar) — UIKit

#### [ビデオ](/jp/design/human-interface-guidelines/tab-bars#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/356)

[](https://developer.apple.com/videos/play/wwdc2025/208)

## [変更履歴](/jp/design/human-interface-guidelines/tab-bars#Change-log)

日付| 変更内容  
---|---  
2025年12月16日| Liquid Glassに関するガイダンスを更新。  
2025年7月28日| Liquid Glassに関するガイダンスを追加。  
2024年9月09日| iPadOS 18でのタブバーを表すアートを追加。  
2024年8月06日| iPadOS 18でのタブバーに関するガイダンスを更新。  
2023年6月21日| visionOSのガイダンスを追加するために更新。
