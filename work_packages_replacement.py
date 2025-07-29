    elif step == 5:
        # Step 5 – Work packages (PREDEFINED SWEDISH)
        info_arrow(
            "Select relevant work packages from the predefined list below. These are standard Swedish work packages (AP 1-15).",
            "Work packages structure the project. Select the packages that are most relevant to your project goals and activities.",
            arrow_key="arrow_wp",
            exp_key="exp_wp",
        )

        # Predefined Swedish work packages (AP 1-15)
        predefined_packages = [
            {"id": "AP1", "name": "Projektledning och koordination", "description": "Övergripande projektledning, koordination av aktiviteter och kommunikation mellan partners"},
            {"id": "AP2", "name": "Forskning och utveckling", "description": "Grundläggande forskning, metodutveckling och teknisk utveckling inom projektområdet"},
            {"id": "AP3", "name": "Pilotprojekt och demonstrationer", "description": "Genomförande av pilotprojekt för att testa och demonstrera utvecklade lösningar"},
            {"id": "AP4", "name": "Utbildning och kompetensutveckling", "description": "Utveckling av utbildningsmaterial, kurser och kompetensutvecklingsaktiviteter"},
            {"id": "AP5", "name": "Nätverksbyggande och samverkan", "description": "Uppbyggnad av nätverk, partnerships och samarbeten mellan olika aktörer"},
            {"id": "AP6", "name": "Kommunikation och spridning", "description": "Kommunikationsaktiviteter, marknadsföring och spridning av projektresultat"},
            {"id": "AP7", "name": "Analys och utvärdering", "description": "Analys av data, utvärdering av aktiviteter och bedömning av projektresultat"},
            {"id": "AP8", "name": "Teknikutveckling och innovation", "description": "Utveckling av ny teknik, innovativa lösningar och tekniska prototyper"},
            {"id": "AP9", "name": "Kapacitetsbyggande", "description": "Uppbyggnad av organisatorisk kapacitet och förmågor hos projektpartners"},
            {"id": "AP10", "name": "Hållbarhetsanalys", "description": "Analys av miljömässiga, sociala och ekonomiska hållbarhetsaspekter"},
            {"id": "AP11", "name": "Användarengagemang", "description": "Engagemang av slutanvändare, intressenter och målgrupper i projektet"},
            {"id": "AP12", "name": "Kvalitetssäkring", "description": "Kvalitetskontroll, standardisering och säkerställande av projektleveranser"},
            {"id": "AP13", "name": "Riskhantering", "description": "Identifiering, analys och hantering av projektrisker och utmaningar"},
            {"id": "AP14", "name": "Ekonomisk planering", "description": "Budgetplanering, kostnadsanalys och ekonomisk uppföljning av projektet"},
            {"id": "AP15", "name": "Resultatrapportering", "description": "Dokumentation, rapportering och presentation av projektresultat och slutsatser"}
        ]

        # Initialize selected work packages in session state
        if "selected_work_packages" not in st.session_state:
            st.session_state.selected_work_packages = []

        st.write("#### Välj relevanta arbetspaket (Work Packages)")
        st.write("Markera de arbetspaket som är mest relevanta för ditt projekt:")

        # Create checkboxes for each predefined work package
        selected_packages = []
        for pkg in predefined_packages:
            is_selected = pkg["id"] in st.session_state.selected_work_packages
            
            if st.checkbox(
                f"**{pkg['id']}: {pkg['name']}**",
                value=is_selected,
                key=f"wp_checkbox_{pkg['id']}",
                help=pkg["description"]
            ):
                selected_packages.append({
                    "id": pkg["id"],
                    "name": pkg["name"],
                    "description": pkg["description"]
                })
                if pkg["id"] not in st.session_state.selected_work_packages:
                    st.session_state.selected_work_packages.append(pkg["id"])
            else:
                if pkg["id"] in st.session_state.selected_work_packages:
                    st.session_state.selected_work_packages.remove(pkg["id"])

        # Show selected packages summary
        if selected_packages:
            st.write(f"**Valda arbetspaket ({len(selected_packages)}):**")
            for pkg in selected_packages:
                st.write(f"• **{pkg['id']}**: {pkg['name']}")
        else:
            st.info("Inga arbetspaket valda ännu. Välj minst ett arbetspaket för att fortsätta.")

        # Save selected work packages to session state in the expected format
        st.session_state.work_packages = selected_packages
        user_input_obj = {"work_packages": selected_packages}
