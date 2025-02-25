"""Data entry template schema for project and energy tabs."""
from pathlib import Path
from pandera import DataFrameSchema, Column, Check, Index
from pandera.engines import pandas_engine
import yaml
# pylint: disable=C0302


def get_project_det_schema() -> DataFrameSchema:
    """
    Create DataFrameSchema for project tab of data entry templates.

    This is the place you should put checks and data validation info

    Returns:
        DataFrameSchema: DataFrameSchema for project
    """
    main_directory = Path(__file__).parents[2]
    with open(
        file=main_directory.joinpath('references/dropdowns.yml'),
        mode='r',
        encoding="utf-8"
    ) as file:
        dropdowns = yaml.safe_load(file)

    project_schema_for_det = DataFrameSchema(
        columns={
            "CLF Firm ID": Column(
                dtype="string",
                checks=None,
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description='CLF Assigned ID for each firm',
                title=None,
            ),
            "CLF Proj ID": Column(
                dtype="string",
                checks=None,
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description='CLF Assigned ID for each project',
                title=None,
            ),
            "Date of Entry": Column(
                dtype=pandas_engine.DateTime(
                    {
                        'format': '%Y/%m/%d'
                    }
                ),
                checks=None,
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description='Date of data entry',
                title=None,
            ),
            "Project Description": Column(
                dtype="string",
                checks=None,
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description='Description of the project focusing on the use, \
function, and scope of work for the project.',
                title=None,
            ),
            "Project State or Province": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('state'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description='State/Province where the project is located',
                title=None,
            ),
            "Project City": Column(
                dtype="string",
                checks=None,
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description='City where the project is located',
                title=None,
            ),
            "Project Zip Code": Column(
                dtype="string",
                checks=None,
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description='5-digit zip code where the project is located',
                title=None,
            ),
            "Project Climate Zone": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('clim_zone'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description='Climate Zone where the project is located',
                title=None,
            ),
            "Building Code": Column(
                dtype="string",
                checks=None,
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description='Governing building code where the project is located',
                title=None,
            ),
            "Energy Code": Column(
                dtype="string",
                checks=None,
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description='Governing energy code where the project is located',
                title=None,
            ),
            "Completion Year": Column(
                dtype="int64",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description="Year of project's actual construction completion, \
certificate of occupancy, or anticipated project completion year",
                title="Completion Year",
            ),
            "Project Type": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('new_reno'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description='Type of construction which details whether the project \
is new or a modification of an existing building',
                title=None,
            ),
            "IBC Construction Type": Column(
                dtype="string",
                checks=[
                    Check.isin(
                        dropdowns.get('const_type')
                    )
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description='Type of construction per IBC',
                title=None,
            ),
            "Attached Parking Type": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('park_type'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description='Type of attached parking structure or “parkade”',
                title=None,
            ),
            "Project Floor Area": Column(
                dtype="float64",
                checks=None,
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description='The total horizontal area occupied by the building including \
attached parking floor area, if applicable, and inclusive of existing floor area, if \
applicable, for renovation projects',
                title=None,
            ),
            "Renovated Floor Area": Column(
                dtype="float64",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description='The total horizontal area where the existing building was renovated',
                title=None,
            ),
            "Added Floor Area": Column(
                dtype="float64",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "External Floor Area": Column(
                dtype="float64",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Attached Parking Floor Area": Column(
                dtype="float64",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Primary Building Use Type": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('bldg_use'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Primary Use Floor Area": Column(
                dtype="float64",
                checks=None,
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Secondary Building Use Type": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('bldg_use'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Secondary Use Floor Area": Column(
                dtype="float64",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Occupant Load": Column(
                dtype="float64",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=False,
                regex=False,
                description=None,
                title=None,
            ),
            "Residential Units": Column(
                dtype="float64",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=False,
                regex=False,
                description=None,
                title=None,
            ),
            "Stories Above Grade": Column(
                dtype="int64",
                checks=None,
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Stories Below Grade": Column(
                dtype="int64",
                checks=None,
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Building Height": Column(
                dtype="float64",
                checks=[
                    Check.greater_than_or_equal_to(min_value=0),
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Thermal Envelope Area": Column(
                dtype="float64",
                checks=[
                    Check.greater_than_or_equal_to(min_value=0.0),
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Window Wall Ratio": Column(
                dtype="float64",
                checks=[
                    Check.greater_than_or_equal_to(min_value=0.0),
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Average R-Value Walls": Column(
                dtype="float64",
                checks=[
                    Check.greater_than_or_equal_to(min_value=0),
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Average R-Value Roofs": Column(
                dtype="float64",
                checks=[
                    Check.greater_than_or_equal_to(min_value=0.0),
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Certifications": Column(
                dtype="string",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Seismic Site Class": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('site_cls'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Seismic Design Category": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('seis_cat'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Ultimate Wind Speed": Column(
                dtype="int64",
                checks=[
                    Check.greater_than_or_equal_to(
                        min_value=80,
                        error='Ultimate Wind Speed must be greater than 80'
                    ),
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Primary Horizontal Gravity System": Column(
                dtype="string",
                checks=[
                    Check.isin(
                        dropdowns.get('horz_sys'),
                        error='Gravity System is not in list'
                    )
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Primary Vertical Gravity System": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('vert_sys'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Primary Lateral Force Resisting System": Column(
                dtype="string",
                checks=[
                    Check.isin(
                        dropdowns.get('lat_sys'),
                        error='Lateral System is not in dropdown list'
                    )
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Podium": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('podium'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Secondary Horizontal Gravity System": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('horz_sys'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Secondary Vertical Gravity System": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('vert_sys'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Typical Column Grid, Long Direction": Column(
                dtype="float64",
                checks=[
                    Check.greater_than_or_equal_to(min_value=0.0),
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Typical Column Grid, Short Direction": Column(
                dtype="float64",
                checks=[
                    Check.greater_than_or_equal_to(min_value=0.0),
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Foundation Type": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('p_fnd_sys'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Final Report": Column(
                dtype="string",
                checks=None,
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Date of Analysis": Column(
                dtype=pandas_engine.DateTime(
                    {
                        'format': '%Y/%m/%d'
                    }
                ),
                checks=None,
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Design Phase": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('prj_phase'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Reference Study Period": Column(
                dtype="int64",
                checks=[
                    Check.equal_to(value=60.0),
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Biogenic Carbon Included": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Software Version": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('software_vrsn'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Purpose of Assessment": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('assess_purp'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Operational Energy Included": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Additional LCA Report Name(s)": Column(
                dtype="string",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Substructure": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Standard Foundations": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Walls for Subgrade Enclosures": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Slabs-on-Grade": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Shell - Superstructure": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Floor Construction": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Roof Construction": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Stairs": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Shell - Exterior Enclosure": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Exterior Walls": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Exterior Windows": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Exterior Doors and Grilles": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Exterior Louvers and Vents": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Exterior Wall Appurtenances": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Roofing": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Roof Appurtenances": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Horizontal Openings": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Overhead Exterior Enclosures": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Interiors - Construction": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Interior Partitions": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Interior Windows": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Interior Doors": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Interior Grilles and Gates": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Raised Floor Construction": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Suspended Ceiling Construction": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Interior Specialties": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Interiors - Finishes": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Wall Finishes": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Floor / Floor Finishes": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Stair Finishes": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Ceiling Finishes": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Sitework": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Roadways": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Surface Parking Lots": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Structured Site Parking": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Plazas and Walkways": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Landscaping": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Tunnels": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "MEP Utilities": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Services (MEP)": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Conveying Systems": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Domestic Water Distribution": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Sanitary Drainage": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Building Support Plumbing Systems": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Process Support Plumbing Systems": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Facility Fuel Systems": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Heating Systems": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Cooling Systems": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "HVAC Distribution Systems": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Ventilation": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Fire Suppression System": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Facility Power Generation": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Electrical Service Distribution": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "General Purpose Electrical Power": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Lighting": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Data Communication Systems": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Electronic Safety Systems": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Integrated Automation Systems": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Equipment & Furnishings": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Commercial Equipment": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Institutional Equipment": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Residential Equipment": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Fixed Furnishings (Casework)": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Movable Furnishings": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "QA User Notes": Column(
                dtype="string",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Embodied Carbon Reductions Pursued": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Embodied Carbon Percent Reduction": Column(
                dtype="float64",
                checks=[
                    Check.greater_than_or_equal_to(min_value=0),
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "Building Reuse": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=False,
                regex=False,
                description=None,
                title=None,
            ),
            "Material Reuse": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=False,
                regex=False,
                description=None,
                title=None,
            ),
            "Alternate Structural System": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=False,
                regex=False,
                description=None,
                title=None,
            ),
            "Structural Biobased Materials": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=False,
                regex=False,
                description=None,
                title=None,
            ),
            "Non-structural Biobased Materials": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=False,
                regex=False,
                description=None,
                title=None,
            ),
            "Structural Element Optimization": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=False,
                regex=False,
                description=None,
                title=None,
            ),
            "Concrete Mix Optimization": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=False,
                regex=False,
                description=None,
                title=None,
            ),
            "Exterior Envelope Optimization": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=False,
                regex=False,
                description=None,
                title=None,
            ),
            "Interior Finishes Optimization": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=False,
                regex=False,
                description=None,
                title=None,
            ),
            "Other Reductions": Column(
                dtype="string",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=False,
                regex=False,
                description=None,
                title=None,
            ),
        },
        checks=None,
        index=Index(
            dtype="string",
            checks=None,
            nullable=False,
            coerce=False,
            name="CLF Model ID",
            description=None,
            title=None,
        ),
        coerce=True,
        strict=True,
        name=None,
        ordered=False,
        unique=None,
        report_duplicates="all",
        unique_column_names=False,
        add_missing_columns=False,
        title=None,
        description=None,
    )
    return project_schema_for_det


def get_energy_det_schema():
    """
    Create  DataFrameSchema for energy tab of data entry templates.

    This is the place you should put checks and data validation info

    Returns:
        DataFrameSchema: DataFrameSchema for project
    """
    main_directory = Path(__file__).parents[2]
    with open(
        file=main_directory.joinpath('references/dropdowns.yml'),
        mode='r',
        encoding="utf-8"
    ) as file:
        dropdowns = yaml.safe_load(file)

    energy_det_schema = DataFrameSchema(
        columns={
            "CLF Firm ID": Column(
                dtype="string",
                checks=None,
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description='CLF Assigned ID for each firm',
                title=None,
            ),
            "CLF Proj ID": Column(
                dtype="string",
                checks=None,
                nullable=False,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description='CLF Assigned ID for each project',
                title=None,
            ),
            "Energy Use Description": Column(
                dtype="string",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "1_Grid Electricity": Column(
                dtype="float64",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "1_Measured Natural Gas": Column(
                dtype="float64",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "1_Measured District": Column(
                dtype="float64",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "1_Measured Other Fossil": Column(
                dtype="float64",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "1_Measured On-site Renewables": Column(
                dtype="float64",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "2_8760 File Name": Column(
                dtype="string",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "2_On-site Renewables Included": Column(
                dtype="string",
                checks=[
                    Check.isin(dropdowns.get('yes_no'))
                ],
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "2_Energy Modeling Tool": Column(
                dtype="string",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "2_Energy Modeling Party": Column(
                dtype="string",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "3_Modeled Grid Electricity": Column(
                dtype="float64",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "3_Modeled Natural Gas": Column(
                dtype="float64",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "3_Modeled District": Column(
                dtype="float64",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "3_Modeled Other Fossil": Column(
                dtype="float64",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "3_Modeled On-site Renewables": Column(
                dtype="float64",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "3_Energy Modeling Tool": Column(
                dtype="string",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "3_Energy Modeling Party": Column(
                dtype="string",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "4_Site pEUI": Column(
                dtype="float64",
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "4_Energy Modeling Tool": Column(
                dtype="string",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
            "4_Energy Modeling Party": Column(
                dtype="string",
                checks=None,
                nullable=True,
                unique=False,
                coerce=False,
                required=True,
                regex=False,
                description=None,
                title=None,
            ),
        },
        checks=None,
        index=Index(
            dtype="string",
            checks=None,
            nullable=False,
            coerce=False,
            name="CLF Model ID",
            description=None,
            title=None,
        ),
        dtype=None,
        coerce=True,
        strict=False,
        name=None,
        ordered=False,
        unique=None,
        report_duplicates="all",
        unique_column_names=False,
        add_missing_columns=False,
        title=None,
        description=None,
    )
    return energy_det_schema
