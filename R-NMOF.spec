#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-NMOF
Version  : 2.1.0
Release  : 29
URL      : https://cran.r-project.org/src/contrib/NMOF_2.1-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/NMOF_2.1-0.tar.gz
Summary  : Numerical Methods and Optimization in Finance
Group    : Development/Tools
License  : GPL-3.0
Requires: R-quadprog
BuildRequires : R-quadprog
BuildRequires : buildreq-R

%description
second edition of "Numerical Methods and Optimization in Finance"
  by M. Gilli, D. Maringer and E. Schumann

%prep
%setup -q -c -n NMOF
cd %{_builddir}/NMOF

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589522720

%install
export SOURCE_DATE_EPOCH=1589522720
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library NMOF
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library NMOF
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library NMOF
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc NMOF || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/NMOF/CITATION
/usr/lib64/R/library/NMOF/DESCRIPTION
/usr/lib64/R/library/NMOF/INDEX
/usr/lib64/R/library/NMOF/Meta/Rd.rds
/usr/lib64/R/library/NMOF/Meta/data.rds
/usr/lib64/R/library/NMOF/Meta/features.rds
/usr/lib64/R/library/NMOF/Meta/hsearch.rds
/usr/lib64/R/library/NMOF/Meta/links.rds
/usr/lib64/R/library/NMOF/Meta/nsInfo.rds
/usr/lib64/R/library/NMOF/Meta/package.rds
/usr/lib64/R/library/NMOF/Meta/vignette.rds
/usr/lib64/R/library/NMOF/NAMESPACE
/usr/lib64/R/library/NMOF/NEWS
/usr/lib64/R/library/NMOF/NMOFex/NMOFdist.R
/usr/lib64/R/library/NMOF/NMOFex/NMOFex.R
/usr/lib64/R/library/NMOF/NMOFex/NMOFman.R
/usr/lib64/R/library/NMOF/NMOFex/README
/usr/lib64/R/library/NMOF/R/NMOF
/usr/lib64/R/library/NMOF/R/NMOF.rdb
/usr/lib64/R/library/NMOF/R/NMOF.rdx
/usr/lib64/R/library/NMOF/book/1ed/C-BinomialTrees/R/EuropeanCall.R
/usr/lib64/R/library/NMOF/book/1ed/C-BinomialTrees/R/EuropeanCallBE.R
/usr/lib64/R/library/NMOF/book/1ed/C-EconometricModels/R/DEabbr.R
/usr/lib64/R/library/NMOF/book/1ed/C-EconometricModels/R/NSf.R
/usr/lib64/R/library/NMOF/book/1ed/C-EconometricModels/R/PSabbr.R
/usr/lib64/R/library/NMOF/book/1ed/C-EconometricModels/R/comparisonLMS.R
/usr/lib64/R/library/NMOF/book/1ed/C-EconometricModels/R/example1.R
/usr/lib64/R/library/NMOF/book/1ed/C-EconometricModels/R/example1b.R
/usr/lib64/R/library/NMOF/book/1ed/C-EconometricModels/R/example2.R
/usr/lib64/R/library/NMOF/book/1ed/C-EconometricModels/R/example3data.R
/usr/lib64/R/library/NMOF/book/1ed/C-EconometricModels/R/example4data.R
/usr/lib64/R/library/NMOF/book/1ed/C-EconometricModels/R/exampleLS.R
/usr/lib64/R/library/NMOF/book/1ed/C-EconometricModels/R/exampleLS2.R
/usr/lib64/R/library/NMOF/book/1ed/C-EconometricModels/R/exampleLoop.R
/usr/lib64/R/library/NMOF/book/1ed/C-EconometricModels/R/exampleRobust.R
/usr/lib64/R/library/NMOF/book/1ed/C-EconometricModels/R/genData.R
/usr/lib64/R/library/NMOF/book/1ed/C-EconometricModels/R/newton.R
/usr/lib64/R/library/NMOF/book/1ed/C-EconometricModels/R/portReg.R
/usr/lib64/R/library/NMOF/book/1ed/C-EconometricModels/R/portRegMV.R
/usr/lib64/R/library/NMOF/book/1ed/C-HeuristicsNutshell/R/fastMA.R
/usr/lib64/R/library/NMOF/book/1ed/C-Introduction/R/equations.R
/usr/lib64/R/library/NMOF/book/1ed/C-ModelingDependencies/R/Gaussian2.R
/usr/lib64/R/library/NMOF/book/1ed/C-ModelingDependencies/R/Spearman.R
/usr/lib64/R/library/NMOF/book/1ed/C-ModelingDependencies/R/randn.R
/usr/lib64/R/library/NMOF/book/1ed/C-ModelingDependencies/R/tria.R
/usr/lib64/R/library/NMOF/book/1ed/C-OptionCalibration/R/callHestoncf.R
/usr/lib64/R/library/NMOF/book/1ed/C-PortfolioOptimization/R/LSabbr.R
/usr/lib64/R/library/NMOF/book/1ed/C-PortfolioOptimization/R/diagonalmult.R
/usr/lib64/R/library/NMOF/book/1ed/C-PortfolioOptimization/R/exampleApply.R
/usr/lib64/R/library/NMOF/book/1ed/C-PortfolioOptimization/R/exampleLS.R
/usr/lib64/R/library/NMOF/book/1ed/C-PortfolioOptimization/R/exampleOF.R
/usr/lib64/R/library/NMOF/book/1ed/C-PortfolioOptimization/R/exampleRatio.R
/usr/lib64/R/library/NMOF/book/1ed/C-PortfolioOptimization/R/exampleSquaredRets.R
/usr/lib64/R/library/NMOF/book/1ed/C-PortfolioOptimization/R/exampleSquaredRets2.R
/usr/lib64/R/library/NMOF/book/1ed/C-PortfolioOptimization/R/frontier.R
/usr/lib64/R/library/NMOF/book/1ed/C-PortfolioOptimization/R/inR.R
/usr/lib64/R/library/NMOF/book/1ed/C-PortfolioOptimization/R/pmcm.R
/usr/lib64/R/library/NMOF/book/1ed/C-PortfolioOptimization/R/portOpt1.R
/usr/lib64/R/library/NMOF/book/1ed/C-PortfolioOptimization/R/portOpt2.R
/usr/lib64/R/library/NMOF/book/1ed/C-PortfolioOptimization/R/portOpt3.R
/usr/lib64/R/library/NMOF/book/1ed/C-PortfolioOptimization/R/repairMatrix.R
/usr/lib64/R/library/NMOF/book/1ed/C-PortfolioOptimization/R/returns.R
/usr/lib64/R/library/NMOF/book/1ed/C-PortfolioOptimization/R/sumSquares.R
/usr/lib64/R/library/NMOF/book/2ed/01_Introduction/R/Introduction.R
/usr/lib64/R/library/NMOF/book/2ed/03_Linear_equations_and_Least_Squares_problems/R/Appendix_linear_systems.R
/usr/lib64/R/library/NMOF/book/2ed/05_Binomial_trees/R/Binomial_Trees.R
/usr/lib64/R/library/NMOF/book/2ed/07_Modeling_dependencies/R/Gaussian2.R
/usr/lib64/R/library/NMOF/book/2ed/07_Modeling_dependencies/R/Spearman.R
/usr/lib64/R/library/NMOF/book/2ed/07_Modeling_dependencies/R/randn.R
/usr/lib64/R/library/NMOF/book/2ed/07_Modeling_dependencies/R/tria.R
/usr/lib64/R/library/NMOF/book/2ed/12_Heuristic_methods_in_a_nutshell/R/Appendix_NMOF_heuristics.R
/usr/lib64/R/library/NMOF/book/2ed/12_Heuristic_methods_in_a_nutshell/R/Heuristics.R
/usr/lib64/R/library/NMOF/book/2ed/13_Heuristics_-_a_tutorial/R/Heuristics_tutorial.R
/usr/lib64/R/library/NMOF/book/2ed/14_Portfolio_optimization/R/Portfolio_Optimization.R
/usr/lib64/R/library/NMOF/book/2ed/15_Backtesting/R/Appendix_parallel.R
/usr/lib64/R/library/NMOF/book/2ed/15_Backtesting/R/Backtesting.R
/usr/lib64/R/library/NMOF/book/2ed/16_Econometric_models/R/Econometric_models.R
/usr/lib64/R/library/NMOF/book/2ed/16_Econometric_models/R/GARCHDEopt.R
/usr/lib64/R/library/NMOF/book/2ed/17_Calibrating_option_pricing_models/R/Option_Calibration.R
/usr/lib64/R/library/NMOF/data/Rdata.rdb
/usr/lib64/R/library/NMOF/data/Rdata.rds
/usr/lib64/R/library/NMOF/data/Rdata.rdx
/usr/lib64/R/library/NMOF/doc/An_overview.R
/usr/lib64/R/library/NMOF/doc/An_overview.Rnw
/usr/lib64/R/library/NMOF/doc/An_overview.pdf
/usr/lib64/R/library/NMOF/doc/DEnss.R
/usr/lib64/R/library/NMOF/doc/DEnss.Rnw
/usr/lib64/R/library/NMOF/doc/DEnss.pdf
/usr/lib64/R/library/NMOF/doc/LSqueens.R
/usr/lib64/R/library/NMOF/doc/LSqueens.Rnw
/usr/lib64/R/library/NMOF/doc/LSqueens.pdf
/usr/lib64/R/library/NMOF/doc/LSselect.R
/usr/lib64/R/library/NMOF/doc/LSselect.Rnw
/usr/lib64/R/library/NMOF/doc/LSselect.pdf
/usr/lib64/R/library/NMOF/doc/NMOF.bib
/usr/lib64/R/library/NMOF/doc/PSlms.R
/usr/lib64/R/library/NMOF/doc/PSlms.Rnw
/usr/lib64/R/library/NMOF/doc/PSlms.pdf
/usr/lib64/R/library/NMOF/doc/TAportfolio.R
/usr/lib64/R/library/NMOF/doc/TAportfolio.Rnw
/usr/lib64/R/library/NMOF/doc/TAportfolio.pdf
/usr/lib64/R/library/NMOF/doc/index.html
/usr/lib64/R/library/NMOF/doc/qTableEx.R
/usr/lib64/R/library/NMOF/doc/qTableEx.Rnw
/usr/lib64/R/library/NMOF/doc/qTableEx.pdf
/usr/lib64/R/library/NMOF/doc/repair.R
/usr/lib64/R/library/NMOF/doc/repair.Rnw
/usr/lib64/R/library/NMOF/doc/repair.pdf
/usr/lib64/R/library/NMOF/doc/vectorise.R
/usr/lib64/R/library/NMOF/doc/vectorise.Rnw
/usr/lib64/R/library/NMOF/doc/vectorise.pdf
/usr/lib64/R/library/NMOF/help/AnIndex
/usr/lib64/R/library/NMOF/help/NMOF.rdb
/usr/lib64/R/library/NMOF/help/NMOF.rdx
/usr/lib64/R/library/NMOF/help/aliases.rds
/usr/lib64/R/library/NMOF/help/paths.rds
/usr/lib64/R/library/NMOF/html/00Index.html
/usr/lib64/R/library/NMOF/html/R.css
/usr/lib64/R/library/NMOF/tests/README
/usr/lib64/R/library/NMOF/unitTests/runTests.R
/usr/lib64/R/library/NMOF/unitTests/test_results.txt
/usr/lib64/R/library/NMOF/unitTests/unitTests2.R
/usr/lib64/R/library/NMOF/unitTests/unitTestsBonds.R
/usr/lib64/R/library/NMOF/unitTests/unitTestsDEopt.R
/usr/lib64/R/library/NMOF/unitTests/unitTestsGAopt.R
/usr/lib64/R/library/NMOF/unitTests/unitTestsInternals.R
/usr/lib64/R/library/NMOF/unitTests/unitTestsLSopt.R
/usr/lib64/R/library/NMOF/unitTests/unitTestsMA.R
/usr/lib64/R/library/NMOF/unitTests/unitTestsOptions.R
/usr/lib64/R/library/NMOF/unitTests/unitTestsPCparity.R
/usr/lib64/R/library/NMOF/unitTests/unitTestsPSopt.R
/usr/lib64/R/library/NMOF/unitTests/unitTestsRestartOpt.R
/usr/lib64/R/library/NMOF/unitTests/unitTestsSAopt.R
/usr/lib64/R/library/NMOF/unitTests/unitTestsTAopt.R
/usr/lib64/R/library/NMOF/unitTests/unitTests_market.R
/usr/lib64/R/library/NMOF/unitTests/unitTests_mc.R
/usr/lib64/R/library/NMOF/unitTests/unitTests_portfolio.R
/usr/lib64/R/library/NMOF/unitTests/unitTestscallCF.R
