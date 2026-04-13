# サイドバー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/sidebars

# サイドバー

ビューの先頭側に表示されるサイドバーを使って、アプリやゲームのセクション間を移動します。

![図案化されたサイドバーの上部。タイトル、セクション、フォルダが表示されています。画像は全体が、6色のオリジナルAppleロゴを連想させる赤色になっています。](https://docs-assets.developer.apple.com/published/c5b43f7b18dbd58d496b32a27dd7d36c/components-sidebar-intro%402x.png)

サイドバーはビューの境界に固定されず、コンテンツ上を移動します。アプリの情報階層が展開された形で表示されるサイドバーは、相対する複数のコンテンツ領域やモードを同時に操作するのに便利です。

サイドバーには、たくさんの縦横のスペースが必要になります。スペースが限られている場合や、ほかの情報や機能のためにもっと画面を割きたい場合は、[タブバー](/jp/design/human-interface-guidelines/tab-bars)のようなコンパクトなコントロールを使用する方が優れたナビゲーション設計になる場合があります。ガイダンスは、[レイアウト](/jp/design/human-interface-guidelines/layout)を参照してください。

## [ベストプラクティス](/jp/design/human-interface-guidelines/sidebars#Best-practices)

**サイドバーの下にあるコンテンツを拡張する。** iOS、iPadOS、macOSでは、ツールバーやタブバーなどほかのコントロールと同様に、サイドバーが[Liquid Glass](/jp/design/human-interface-guidelines/materials#Liquid-Glass)レイヤー内でコンテンツ上を移動します。サイドバーの分離して浮いているような見た目を強化するため、横方向にスクロール可能にするか、背景拡張ビューを適用して、サイドバーの下にあるコンテンツを拡張します。これによって、隣接するコンテンツがミラーリングされ、サイドバーの下にあるコンテンツが引き伸ばされたような印象になります。デベロッパ向けのガイダンスは、[`backgroundExtensionEffect()`](/documentation/SwiftUI/View/backgroundExtensionEffect\(\))を参照してください。

![iPadのアプリの左側。画像がウインドウの上方に広がっていますが、サイドバーの境界で切れています。](https://docs-assets.developer.apple.com/published/6b6c7d4a8cd876f7ee0533a36c8a9104/sidebars-extend-content-beneath-sidebar-incorrect%402x.png)

![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![iPadのアプリの左側。画像がウインドウの上方に広がり、サイドバーの下にある部分には反転、ぼかし、拡大を行う背景拡張エフェクトが適用され、ウインドウの境界にまで達しています。](https://docs-assets.developer.apple.com/published/655ddde579e3789061a15a42e8fe9b61/sidebars-extend-content-beneath-sidebar-correct%402x.png)

![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

**可能な場合は、ユーザによるサイドバーのコンテンツのカスタマイズに対応する。** サイドバーでアプリの重要な領域間を簡単に移動できるので、どの領域が最も重要で、どういう順番で表示するかをユーザが決定できるようにするとさらに効果的です。

**アプリのコンテンツが多い場合は、開閉コントロールで階層をグループ化する。**[開閉コントロール](/jp/design/human-interface-guidelines/disclosure-controls)は、サイドバーの縦方向のスペースを管理しやすい状態に維持するのに役立ちます。

**サイドバーの項目をユーザに馴染みのあるシンボルで表す。**[SF Symbol](/jp/design/human-interface-guidelines/sf-symbols)が提供するカスタマイズ可能なさまざまなシンボルでアプリ内の項目を表現できます。カスタムアイコンを使用する必要がある場合は、ビットマップ画像を使うより、[カスタムシンボル](/jp/design/human-interface-guidelines/sf-symbols#Custom-symbols)を作成することをおすすめします。SF Symbolsアプリは[Appleデザインリソース](https://developer.apple.com/design/resources/#sf-symbols)からダウンロードしてください。

**サイドバーをユーザが非表示にできるようにする。** コンテンツ詳細のためのスペースを空けたり、気を散らすものを減らしたりするために、ユーザはサイドバーを非表示にしたい場合があります。可能な場合は、ユーザがすでに知っているプラットフォーム固有の操作で、サイドバーの表示/非表示を切り替えてください。例えばiPadOSでユーザが期待する操作は、端からスワイプするシステム組み込みのジェスチャです。macOSでは、表示/非表示ボタンを含めるか、アプリの「表示」メニューに「サイドバーを表示」と「サイドバーを非表示」コマンドを追加できます。visionOSでは、ウインドウは通常、サイドバーを表示するために広がります。そのため、ユーザがサイドバーを非表示にする必要はめったにありません。サイドバーを見つけやすくするため、デフォルトではサイドバーを非表示にしないでください。

**基本的に、サイドバーで表示する階層は2つまでとする。** データ階層が3つ以上になる場合は、サイドバーの項目と詳細ビューの間にコンテンツリストを含む分割ビューのインターフェイスを使用することを検討します。

**サイドバーに2つの階層を含める必要がある場合は、各グループに簡潔で分かりやすいラベルを付ける。** ラベルを短くするため、不要な語句は省略します。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/sidebars#Platform-considerations)

 _tvOSに追加の考慮事項はありません。watchOSには対応していません。_

### [iOS](/jp/design/human-interface-guidelines/sidebars#iOS)

**なるべくサイドバーを使用しない。** サイドバーは横向きで多くのスペースを占有し、縦向きでは利用できません。代わりに、使うスペースが少なく、どちらの向きでも表示される[タブバー](/jp/design/human-interface-guidelines/tab-bars)の利用を検討してください。

### [iPadOS](/jp/design/human-interface-guidelines/sidebars#iPadOS)

[`sidebarAdaptable`](/documentation/SwiftUI/TabViewStyle/sidebarAdaptable)スタイルのタブビューを使ってサイドバーを表示する場合は、アプリを開くときに、サイドバーで表示するかタブバーで表示するかを選択します。どちらを選んでも、表示を切り替えるボタンが含まれます。このスタイルは、デバイスの回転やウインドウのサイズ変更にも自動的に対応し、ビューの幅によく合う形式でコントロールが表示されます。

デベロッパ向けの備考

サイドバーのみを表示するには、[`NavigationSplitView`](/documentation/SwiftUI/NavigationSplitView)を使用して分割ビューのプライマリパネルにサイドバーを表示するか、[`UISplitViewController`](/documentation/UIKit/UISplitViewController)を使用します。

**最初にタブバーを使うことを検討する。** タブバーを使うとコンテンツの表示に使えるスペースが広がり、多数のアプリのメイン領域間をスムーズに移動できるようになります。タブバーには収まらない広いスペースが必要な場合は、サイドバーに変換できるタブバーのスタイルを使うと、利用頻度が低いコンテンツにアクセスできるようになります。ガイダンスは、[タブバー](/jp/design/human-interface-guidelines/tab-bars)を参照してください。

**必要に応じて、サイドバーの見た目を調整する。** SwiftUIを使用せずにサイドバーを作成する場合は、コレクションビューのリストレイアウトにある[`UICollectionLayoutListConfiguration.Appearance.sidebar`](/documentation/UIKit/UICollectionLayoutListConfiguration-swift.struct/Appearance-swift.enum/sidebar)の見た目から選べます。デベロッパ向けのガイダンスは、[`UICollectionLayoutListConfiguration.Appearance`](/documentation/UIKit/UICollectionLayoutListConfiguration-swift.struct/Appearance-swift.enum)を参照してください。

### [macOS](/jp/design/human-interface-guidelines/sidebars#macOS)

サイドバーの行の高さ、テキスト、グリフのサイズは、全体の高さ（スモール、ミディアム、ラージのいずれか）によって決まります。プログラムでサイズを設定することもできます。ユーザも、「一般」設定で、異なるサイドバーのアイコンサイズを選択できます。

**アプリの柔軟性が失われるので、サイドバーのアイコンの色を固定しない。** デフォルトでは、サイドバーのアイコンには現在の[アクセントカラー](https://developer.apple.com/jp/design/human-interface-guidelines/color#App-accent-colors)が使用されます。ほとんどのユーザは、自分の選択したアクセントカラーがすべてのアプリで使用されると考えます。色を固定するとアイコンの意味が明確になるとはいえ、サイドバーのアイコンには、ほぼ例外なく、ユーザが選択した色を表示することをおすすめします。

**コンテナウインドウのサイズ変更に応じて自動的にサイドバーの表示/非表示を切り替える。** 例えば「メール」では、表示ウインドウのサイズを小さくすると、サイドバーが自動的に折りたたまれて、メッセージコンテンツの領域が確保されます。

**サイドバーの下部には重要な情報やアクションを表示しない。** ユーザがウインドウを移動したときに下の部分が隠れてしまうことがよくあるためです。

### [visionOS](/jp/design/human-interface-guidelines/sidebars#visionOS)

**アプリの階層が深い場合は、タブバー内のタブでサイドバーを使用することを検討する。** この状況では、サイドバーによってタブ内での2次的なナビゲーションが可能になります。タブでサイドバーを使用する場合は、サイドバーでの選択によって表示中のタブが変わらないようにしてください。

![visionOSのミュージックアプリのスクリーンショットの一部。アプリのウインドウには、ミュージックライブラリに移動するためのサイドバーが含まれています。第2パネルにはプレイリストのグリッドが含まれています。](https://docs-assets.developer.apple.com/published/5e381525f4cccac8e9eb979fe4c984c6/visionos-sidebar-music%402x.png)

## [リソース](/jp/design/human-interface-guidelines/sidebars#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/sidebars#Related)

[分割ビュー](/jp/design/human-interface-guidelines/split-views)

[タブバー](/jp/design/human-interface-guidelines/tab-bars)

[レイアウト](/jp/design/human-interface-guidelines/layout)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/sidebars#Developer-documentation)

[`sidebarAdaptable`](/documentation/SwiftUI/TabViewStyle/sidebarAdaptable) — SwiftUI

[`NavigationSplitView`](/documentation/SwiftUI/NavigationSplitView) — SwiftUI

[`sidebar`](/documentation/SwiftUI/ListStyle/sidebar) — SwiftUI

[`UICollectionLayoutListConfiguration`](/documentation/UIKit/UICollectionLayoutListConfiguration-swift.struct) — UIKit

[`NSSplitViewController`](/documentation/AppKit/NSSplitViewController) — AppKit

#### [ビデオ](/jp/design/human-interface-guidelines/sidebars#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/208)

## [変更履歴](/jp/design/human-interface-guidelines/sidebars#Change-log)

日付| 変更内容  
---|---  
2025年6月09日| サイドバーの下にあるコンテンツの拡張に関するガイダンスを追加。  
2024年8月06日| SwiftUIのアダプティブなサイドバースタイルを追加するためにガイダンスを更新。  
2023年12月05日| iPadOSのアートワークを追加。  
2023年6月21日| visionOSのガイダンスを追加するために更新。
