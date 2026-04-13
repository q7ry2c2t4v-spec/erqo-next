# Dockメニュー

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/dock-menus

# Dockメニュー

Macでは、Dockにあるアプリやゲームのアイコンを副ボタンでクリックするとDockメニューが開きます。Dockメニューには、システムが提供する項目とカスタム項目の両方が含まれます。

![Dockにあるアイコンから伸びる図案化されたメニュー。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/c36a926b4f0b0a4687d6e3e23b334812/components-dock-menu-intro%402x.png)

システムが提供するDockメニューの項目は、そのアプリが開いているかどうかで異なる可能性があります。例えばSafariのDockメニューには、現在のウインドウを表示したり、新しいウインドウを開いたりできるメニュー項目があります。

備考

iOSおよびiPadOSはDockメニューに対応していませんが、ユーザはシステムが提供する項目とカスタム項目で構成される類似のメニューを利用できます。これは、ホーム画面のクイックアクションと呼ばれ、ホーム画面またはDockでアプリアイコンを長押しすると表示されます。ガイダンスは、[ホーム画面にクイックアクションを追加する](/jp/design/human-interface-guidelines/home-screen-quick-actions)を参照してください。

## [ベストプラクティス](/jp/design/human-interface-guidelines/dock-menus#Best-practices)

ほかのすべてのメニューと同様、Dockのメニュー項目に簡潔なラベルを付け、それらを論理的に並べる必要があります。ガイダンスは[メニュー](/jp/design/human-interface-guidelines/menus)を参照してください。

**Dockメニューのカスタム項目はほかの場所からも利用できるようにする。** Dockメニューを使用しない人もいるので、メニューバーのメニューやアプリのインターフェイス内など、ほかの場所でも同じコマンドを提供することが重要です。

**Dockメニューにはなるべく有用性の高いカスタム項目を表示する。** 例えば、Dockメニューに現在開いているすべてのウインドウや最近開いたウインドウのリストを表示すれば、ユーザが目的のウインドウにすぐにジャンプできるので便利です。アプリが最前面にない場合や開いているウインドウがない場合に役立ちそうなアクションをいくつか表示することもおすすめです。例えば「メール」のDockメニューには、開いているすべてのウインドウのリストに加えて、新規メールの受信や新規メッセージの作成のための項目があります。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/dock-menus#Platform-considerations)

 _iOS、iPadOS、tvOS、visionOS、watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/dock-menus#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/dock-menus#Related)

[メニュー](/jp/design/human-interface-guidelines/menus)

[ホーム画面のクイックアクション](/jp/design/human-interface-guidelines/home-screen-quick-actions)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/dock-menus#Developer-documentation)

[`applicationDockMenu(_:)`](/documentation/AppKit/NSApplicationDelegate/applicationDockMenu\(_:\)) — AppKit
