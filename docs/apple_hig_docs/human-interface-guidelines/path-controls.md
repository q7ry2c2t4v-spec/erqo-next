# パスコントロール

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/path-controls

# パスコントロール

パスコントロールは、選択されているファイルまたはフォルダのファイルシステムパスを表示します。

![図案化されたパスコントロール。「ヒューマンインターフェイスガイドライン」書類のルートディスク、親フォルダ、選択項目を示しています。画像は全体が、6色のオリジナルAppleロゴを連想させる赤色になっています。](https://docs-assets.developer.apple.com/published/4241a3d95ada2555b713ed0edbed8aa6/components-path-control-intro%402x.png)

例えば、Finderで「表示」＞「パスバーを表示」と選択すると、ウインドウの下部にパスバーが表示されます。パスバーには、選択した項目のパスか、何も選択されていない場合はウインドウのフォルダのパスが表示されます。

パスコントロールには、2つのスタイルがあります。

![Finderのパスバー。4つの場所の階層構造が示されています。](https://docs-assets.developer.apple.com/published/da232cfbe445ade26eb375a13da8b165/path-controls-standard%402x.png)

**標準:** ルートディスク、親フォルダ、選択した項目が直線状に並んだリストです。各項目には、アイコンと名前が表示されています。リストが長すぎてコントロールに収まらない場合は、最初と最後の項目の間の名前が非表示になります。コントロールを編集可能にすると、項目をコントロールにドラッグできるようになります。この操作で項目が選択され、パスがコントロールに表示されます。

![パスコントロール。フォルダアイコンとポップアップコントロールが表示されています。](https://docs-assets.developer.apple.com/published/be76739512c55e980f406f70a4fbeba0/path-controls-popup%402x.png)

**ポップアップ:** [ポップアップボタン](https://developer.apple.com/jp/design/human-interface-guidelines/pop-up-buttons)に似たコントロールで、選択した項目のアイコンと名前が表示されます。項目をクリックすると、ルートディスク、親フォルダ、選択した項目を含むメニューが開きます。コントロールを編集可能にすると、メニューに追加の選択コマンドが表示されます。このコマンドを使用して項目を選択し、コントロールに表示することができます。項目をコントロールにドラッグして、項目の選択とパスの表示を行うこともできます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/path-controls#Best-practices)

**パスコントロールはウインドウフレームではなくウインドウ本体で使用する。** パスコントロールはツールバーやステータスバーで使うコンポーネントではありません。Finderのパスコントロールは、ステータスバーではなくウインドウ本体の下部に表示される点に注意してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/path-controls#Platform-considerations)

 _iOS、iPadOS、tvOS、visionOS、watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/path-controls#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/path-controls#Related)

[ファイルの管理](/jp/design/human-interface-guidelines/file-management)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/path-controls#Developer-documentation)

[`NSPathControl`](/documentation/AppKit/NSPathControl) — AppKit
