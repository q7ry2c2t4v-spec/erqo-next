# タブビュー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/tab-views

# タブビュー

タブビューは、相互排他的な複数のコンテンツパネルを同じ領域に表示します。ユーザは、タブコントロールを使ってパネル間を切り替えることができます。

![図案化された2個のラベル付きタブからなるビュー。1個目のタブが選択されています。画像全体が、6色の初代Appleロゴの赤色を連想させる赤みを帯びています。](https://docs-assets.developer.apple.com/published/f4e3a02f3257eb79b0a3a043708b4e42/components-tab-view-intro%402x.png)

## [ベストプラクティス](/jp/design/human-interface-guidelines/tab-views#Best-practices)

**互いに関連の深いコンテンツ領域を表示するときに使用する。** タブビューはその見た目上、内容同士にまとまりがあることが視覚的に強く感じられます。ユーザは、それぞれのタブに表示される内容の間に何らかの類似性や関連性があるという印象を持ちます。

**パネル内のコントロールは同じパネル内にのみ影響するようにする。** パネルは相互に排他的なので、ほかのパネルに影響が及ばないようにします。

**それぞれのタブにはパネルの内容を表すラベルを指定する。** タブをクリックまたはタップせずともパネルの内容を予測できるのがよいラベルです。タブのラベルには基本的に名詞または短い名詞句を使用します。コンテキストによっては、動詞や短い動詞句が理にかなっている場合もあるかもしれません。タブのラベルには、タイトルスタイルの大文字化を使用します。

**タブの切り替え用にポップアップボタンを使うのは避ける。** タブコントロールが効率的なのは、1回のクリックやタップで選択できるからです。一方、ポップアップボタンには2回の操作が必要です。また、タブコントロールでは画面にすべての選択肢が同時に表示されますが、ポップアップボタンではボタンをクリックしないと選択肢を確認できません。なお、コンテンツを表示するパネルが多すぎてタブ表示が合理的でない場合には、代わりにポップアップボタンを使うことが妥当なケースもあります。

**タブビューに配置するタブは5個までにする。** タブの数が6個以上になると圧迫感が生じ、レイアウトの問題も発生する可能性があります。6個以上のタブが必要な場合は、別の方法でユーザインターフェイスを実装することを検討してください。例えば、各タブをポップアップボタンメニューのビューオプションとして表示するなどします。

デベロッパ向けのガイダンスは、[`NSTabView`](/documentation/AppKit/NSTabView)を参照してください。

## [構造](/jp/design/human-interface-guidelines/tab-views#Anatomy)

タブコントロールはコンテンツ領域の上端に表示されます。コントロールを非表示にすることを選択できます。これは、パネルの切り替えをプログラム側で行うアプリに適しています。

![ウインドウの図。3個のタブがあるタブコントロールが、コンテンツビューの上端に中央揃えで配置されています。](https://docs-assets.developer.apple.com/published/2cfd307117e12e033426800038063986/tab-views-top%402x.png)

タブコントロールを非表示にする場合は、コンテンツ領域を境界線なし、ベゼルあり、境界線ありのいずれかにすることができます。境界のないビューは、塗りつぶすことも、透明にすることもできます。

**基本的にタブビューの上下左右にウインドウボディ領域のマージンを残してタブビューをはめ込む。** このようにレイアウトすると、見た目がすっきりし、タブビューの内容に直接関係しないコントロールを追加する余地も残ります。ウインドウの端までタブビューを広げることもできますが、このレイアウトは一般的ではありません。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/tab-views#Platform-considerations)

 _iOS、iPadOS、tvOS、visionOSには対応していません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/tab-views#iOS-iPadOS)

類似した機能を実現するには、[セグメントコントロール](https://developer.apple.com/jp/design/human-interface-guidelines/segmented-controls)の使用を検討してください。

### [watchOS](/jp/design/human-interface-guidelines/tab-views#watchOS)

watchOSのタブビューは、[ページコントロール](https://developer.apple.com/design/human-interface-guidelines/components/presentation/page-controls)を使用して表示されます。デベロッパ向けのガイダンスは、[`TabView`](/documentation/SwiftUI/TabView)および[`verticalPage`](/documentation/SwiftUI/TabViewStyle/verticalPage)を参照してください。

![Apple Watchの図。Digital Crownの横にページコントロールがあります。現在のコンテンツをスクロールできることと、ページ間をスクロールできることを示すため、現在のドットが拡大されています。](https://docs-assets.developer.apple.com/published/f85b646fa8744c101775c08b95897385/tab-view-watch-vertical%402x.png)

## [リソース](/jp/design/human-interface-guidelines/tab-views#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/tab-views#Related)

[タブバー](/jp/design/human-interface-guidelines/tab-bars)

[セグメントコントロール](/jp/design/human-interface-guidelines/segmented-controls)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/tab-views#Developer-documentation)

[`TabView`](/documentation/SwiftUI/TabView) — SwiftUI

[`NSTabView`](/documentation/AppKit/NSTabView) — AppKit

## [変更履歴](/jp/design/human-interface-guidelines/tab-views#Change-log)

日付| 変更内容  
---|---  
2023年6月05日| watchOSでのタブビューの使用に関するガイダンスを追加。
