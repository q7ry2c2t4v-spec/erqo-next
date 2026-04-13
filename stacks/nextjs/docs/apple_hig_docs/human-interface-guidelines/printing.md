# プリント

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/printing

# プリント

iOS、iPadOS、macOS、visionOSのアプリには、システムが提供するプリント機能を適宜組み込むことができます。また、必要な場合は、プリンタや書類に固有のカスタムオプションを表示できます。

![プリンタのスケッチ。プリントを示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせるオレンジ色になっています。](https://docs-assets.developer.apple.com/published/5d73ea26519819f19545c439150bb4b5/patterns-printing-intro%402x.png)

## [ベストプラクティス](/jp/design/human-interface-guidelines/printing#Best-practices)

**プリント機能を見つけやすくする。** プリントアクションを見つけやすくするため、標準のシステムの場所に配置します。例えばmacOSアプリなら、「ファイル」メニューに「プリント」項目を含めます。iOSやiPadOSのアプリなら、ツールバーに[アクションシート](https://developer.apple.com/jp/design/human-interface-guidelines/action-sheets)を開くボタンを追加します。macOSのアプリにツールバーがある場合は、そこにも「プリント」ボタンを配置できます。ただし、このボタンはオプションにして、ユーザがツールバーをカスタマイズするときに追加できるようにすることを検討してください。

**プリントオプションは可能な場合のみ表示する。** 画面にプリントするものがない場合や、プリンタが利用できない場合は、macOSアプリの「ファイル」メニューの「プリント」項目を暗くします。iOSとiPadOSのアプリの場合は、アクションシートから「プリント」アクションを削除します。カスタムのプリントボタンを実装する場合は、プリントできないときに暗くするか非表示にします。

**関連するプリントオプションを表示する。** ページ範囲の選択、複数部数のプリント、両面プリントなどのオプションが妥当で、プリンタがそれに対応している場合は、システムが提供するビューを使用してこれらのオプションを表示します。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/printing#Platform-considerations)

 _iOS、iPadOS、visionOSに追加の考慮事項はありません。tvOSとwatchOSには対応していません。_

### [macOS](/jp/design/human-interface-guidelines/printing#macOS)

**macOSのアプリケーションでシステムが提供しないアプリケーション固有のプリントオプションを提供する場合は、プリントパネルでカスタムのカテゴリを作成することを検討する。** デフォルトで、プリントパネルには「レイアウト」、「用紙処理」、「メディアと品質」などの複数カテゴリの設定が含まれています。カスタムのカテゴリには、アプリの名前など独自の名前を設定し、アプリで優れたプリント体験を利用できるようにするオプションを含めます。例えばKeynoteでは、発表者ノート、スライドの背景、スキップしたスライドのプリントなど、プレゼンテーション固有のオプションを提供しています。

**アプリで書類に固有なページ設定に対応する場合は、ページ設定ダイアログを表示することを検討する。** _ページ設定ダイアログ_ には、用紙サイズ、向き、拡大縮小など、特定の書類のプリントに適用されるあまり変更されない設定を含めます。特に理由がない限り、システムですでに提供されている機能をアプリで実装しないようにしてください。例えば、ページの向きの変更や逆順でプリントなどのオプションは、システムで実装されているので、含める必要はありません。

**オプション間の依存関係を明確にする。** 例えば、両面プリントが使用可能な場合は、透明な媒体にプリントするオプションは利用できなくします。

**よく使用する機能と高度な機能を分ける。** 開閉コントロールを使用し、詳細オプションは必要になるまで表示しないようにすることをおすすめします。また、詳細オプションには、 _詳細オプション_ というラベルを付けます。

**設定の効果をプレビューできるようにすることを検討する。** 例えば、サムネール画像を更新して、トーンコントロールを変更したときの効果を表示できるようにします。

**対象の書類について変更した設定を保持することを検討する。** ユーザが再度プリントする場合に備えて、少なくとも書類を閉じるまではプリント設定を保存するようにします。

## [リソース](/jp/design/human-interface-guidelines/printing#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/printing#Related)

[ファイルの管理](/jp/design/human-interface-guidelines/file-management)

[「ファイル」メニュー](/jp/design/human-interface-guidelines/the-menu-bar#File-menu)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/printing#Developer-documentation)

[`UIPrintInteractionController`](/documentation/UIKit/UIPrintInteractionController) — UIKit

[`NSDocument`](/documentation/AppKit/NSDocument) — AppKit
